@Library('sstk-pipeline-plugin')

import static com.shutterstock.Container.*
import static com.shutterstock.PipelineOptions.*
import com.shutterstock.PipelineOptions


// create pipeline objects
def jpp = sstk(this, 'pipeline', '2.0')
def githubUtils = sstk(this, 'github-utils')


//select build image
def baseContainer = fromDockerHub('base-image', 'python:alpine3.7')

//define paramaters & variables for use in this Jenkins job
def nodeOptions = [:]
def buildOptions = [:]
def commitId
Boolean isEphemeral = false
Boolean isPr = false

//Not saving workspace. (default is true)
nodeOptions.put('saveWorkspace', false)
nodeOptions.put('restoreWorkspace', false)

//Set minimum version required to operate with GS clusters
jpp.genericHttpVersion = '^2.1.4'



// build phase. Includes running pre-build checks such as Quality Gates checks and Security Scans.
sstkNode(nodeOptions, 'build', [ baseContainer ]) {
  checkout scm
  githubUtils.initialize()
  commitId = githubUtils.getCommit()
  isPr = !!githubUtils.getPrNumber()
  if (isPr) {
    isEphemeral = true
  }
  Integer prNumber = githubUtils.getPrNumber()
  commitId = githubUtils.getCommit();
  jpp.initialize(fromGitHub(githubUtils))
  container(baseContainer.getName()) {
    jpp.sstkStage(type: 'buildImage', name: 'Build & Publish Image') {
        jpp.buildAndPublishImage(buildOptions) // This method with also run a securityscan using a tool called Snyk.
  }
}
}

jpp.imageId = commitId
// Deploy to all envs (this example only deploys to dev, but true application deployments would deploy to DEV, QA and PROD)
Map deployClusters = [dev: 'eks-playground-a-playground-a'] // In GS clusters, applications should use 'gs-auto' instead of actual clusterID
List deployEnvs = ['dev'] //List envs = ['dev', 'qa', 'prod']
deployEnvs.each { env ->
  if (env == 'prod' && branch != 'master') skip // Only deploy master branch to production env
  nodeOptions.put('clusterIds', [deployClusters[env]])
  sstkNode(nodeOptions, env, [baseContainer]) {
    checkout scm
    jpp.sstkStage(type: "${env}Deploy", name: "Deploy to ${env}") {
      if (env == 'prod' && branch == 'master') {
        jpp.manualVerification(
        approvalRequiredMessage: 'Manual approval required before deploying to production',
        approvalPromptMessage: 'Deploy to production?',
        slackChannel: 'pipeline-examples')
      }
      String appFqdn = jpp.deployGenericHttp('deploy', isEphemeral)
      jpp.awaitURLReadiness(appFqdn)
    }
    jpp.sstkStage(type: "${env}PostDeploy", name: "Tag Image") {
      jpp.addTagToImage()
    }
  }
}