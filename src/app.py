from flask import Flask, render_template


app = Flask(__name__) # helps determine the root path

@app.route('/') # homepage of website
def index():
    return 'This is the homepage'

@app.route('/about')
def about():
    return '<h2>This is the about page of the website</h2>'

@app.route('/addingitem')
def adding_item():
    for i in range(0,3):
        list1.append(input("Enter an item in your to-do list: "))
    return str(list1)

@app.route('/removingitem')
def remove_item():
    item_to_remove_from_list = input("What item do you wish to remove from the list?")
    list1.remove(item_to_remove_from_list)
    return str(list1)

@app.route("/health", methods=['GET'])
def health_ep():
    return 'Health : Excellent'
    

if __name__ == "__main__": # Start the server
    list1 = []
    app.run(debug=True)
