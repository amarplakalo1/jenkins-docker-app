from flask import Flask


app = Flask(__name__) # helps determine the root path

@app.route('/') # homepage of website
def index():
    return 'This is the homepage'

@app.route('/about')
def about():
    return '<h2>This is the about page</h2>'


if __name__ == "__main__": # Start the server
    app.run(debug=True)

