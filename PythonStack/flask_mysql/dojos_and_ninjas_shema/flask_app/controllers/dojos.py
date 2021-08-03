from flask_app import app
from flask_app.models.dojo import Dojo
from flask import render_template,redirect,request,flash

@app.route('/dojos')
def show_all_dojos():
    dojos = Dojo.select_all()
    return render_template('dojos.html', all_dojos = dojos)

@app.route('/process', methods=["POST"])
def create_dojo():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "dojo_name": request.form["dojo_name"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    Dojo.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/dojos')