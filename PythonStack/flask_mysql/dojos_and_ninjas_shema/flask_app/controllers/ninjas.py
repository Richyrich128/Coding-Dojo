from flask import render_template, redirect, request, flash
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def dojo_index():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("index.html", all_dojos = dojos)