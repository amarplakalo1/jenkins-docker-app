import os
from django.shortcuts import render
from flask import Flask, redirect, render_template


app = Flask(__name__) # helps determine the root path

@app.route('/') # homepage of website
def index():
    menu_choice = 0
    while menu_choice != 1 and menu_choice != 2:
        print("Welcome to your to-do list. Pick any option from the menu : ")
        print("1.Add item: ")
        print("2.Remove item: ")
        print("3.View items: ")
        menu_choice = int(input("Enter menu choice "))

        if menu_choice == 1:
            return redirect("/addingitem", code=302)
        elif menu_choice == 2:
            return redirect("/removingitem", code=302)
        elif menu_choice == 3:
            return redirect("/viewitems", code=302)

    return 'This is the homepage'

@app.route('/about')
def about():
    return render_template("adding_item.html")

@app.route('/addingitem')
def adding_item():
    for i in range(0,3):
        list1.append(input("Enter an item in your to-do list: "))
    return redirect("/", code=302)

@app.route('/removingitem')
def remove_item():
    item_to_remove_from_list = input("What item do you wish to remove from the list?")
    list1.remove(item_to_remove_from_list)
    return redirect("/", code=302)

@app.route('/viewitems')
def view_items():
    print(list1)
    return redirect("/", code=302)

@app.route("/health", methods=['GET'])
def health_ep():
    return 'Health : Excellent'

if __name__ == "__main__": # Start the server
    list1 = []
    app.run(debug=True)
