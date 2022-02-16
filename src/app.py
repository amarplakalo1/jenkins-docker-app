import os
from django.shortcuts import render
from flask import Flask, redirect, render_template, request


app = Flask(__name__) # helps determine the root path

@app.route('/') # homepage of website
def index():
    return render_template("homepage.html")

@app.route('/about')
def about():
    return "This app allows you to add items to the to-do list, remove them or to view your to-do list"
@app.route('/addingitem', methods=['POST', 'GET'])
def adding_item():
    if request.method == 'POST':
        item_to_add = request.form["item_to_add_input_field"]
        list1.append(item_to_add)
    return render_template("adding_item.html")

@app.route('/removingitem', methods=['POST', 'GET'])
def remove_item():
    if request.method == 'POST':
        item_to_remove = request.form["item_to_remove_input_field"]
        list1.remove(item_to_remove)
    return render_template("removing_item.html")

@app.route('/viewitems')
def view_items():
    return render_template("viewing_items.html",list1=list1)

@app.route("/health", methods=['GET'])
def health_ep():
    return 'Health : Excellent'

if __name__ == "__main__": # Start the server
    list1 = []
    app.run(host="0.0.0.0", port="8080", debug=True)
