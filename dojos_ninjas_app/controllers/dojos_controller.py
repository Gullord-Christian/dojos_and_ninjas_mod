from dojos_ninjas_app import app
from flask import render_template, redirect, request
from dojos_ninjas_app.models.dojos_model import Dojo


@app.route("/")
@app.route('/dojos/create')
def display_create_dojos():
    #Executing classmethod get_all_dojos on dojos_model.py from database table dojos
    dojos = Dojo.get_all_dojos()
    return render_template("create_dojo.html", dojos = dojos)
    


@app.route("/dojos/create", methods=["POST"])
def create_dojo():
    ### not sure why I am getting an error here on line 18 when trying to create a new dojo
    data = {
        "dojo_name" : request.form["dojo_name"]
    }
    Dojo.create(data)
    return redirect ('/dojos/create')


@app.route('/dojo/<int:id>')
def display_dojo_ninjas(id):
    data = {
        'id' : id
    }
    new_dojo = Dojo.get_all_ninjas(data)
    return render_template("show_dojos.html", new_dojo = new_dojo)


"""
GET - read and display
URL of the route to display all: the name of the list or dictionary that we are about to display
Example: "/todos"
Example: "/users 

Function: get_all_todos()

URL of the route to display one: the name of the list in singular that we are about to display
followed by the id
Example: "/todo/<int:id>"
Example: "/user/<int:id>"

Function: get_todo_by_id( id )

POST - create
URL of the route to create something new: the name of the list in singular that we are about to create
followed by the keyword /new
Example: "/todo/new"
Example: "/user/new

Function: create_todo()

PUT - update
URL of the route to update something already existing: the name of the list in singular that we are about 
to update, followed by the id, followed by the keyword /update /edit
Example: "/todo/<int:id>/update"
Example: "/user/<int:id>/update"

Function: update_todo_by_id( id )

DELETE - remove
URL of the route to delete something already existing: the name of the list in singular that we are about 
to delete, followed by the id, followed by the keyword /delete /remove
Example: "/todo/<int:id>/delete"
Example: "/user/<int:id>/remove"

Function: delete_todo_by_id( id )

"""