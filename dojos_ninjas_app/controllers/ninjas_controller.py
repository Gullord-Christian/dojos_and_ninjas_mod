from dojos_ninjas_app import app
from flask import render_template, redirect, request
from dojos_ninjas_app.models.ninjas_model import Ninja
from dojos_ninjas_app.models.dojos_model import Dojo


@app.route('/ninja/new')
def display_create_ninja():
    #Executing classmethod get_all_dojos on dojos_model.py
    return render_template("new_ninja.html", dojos = Dojo.get_all_dojos())

        ## adding ninja with a post method via the ninja/new route, added into the ninja table
@app.route("/ninja/new", methods=["POST"])
def create_ninja():
    data = {
        "dojo_id" : request.form["dojo_id"],
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"],
    }

    Ninja.create(data)
    return redirect ("/dojos/create")