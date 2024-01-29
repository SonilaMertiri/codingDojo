from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


# @app.route('/ninja/dojo')
# def show_ninjas_of_dojo():
#     ninja=

@app.route('/add/ninja', methods=['POST'])
def add_ninja():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_id']
    }
    # Save the new ninja
    Ninja.save(data)
    return redirect('/')

@app.route('/add/ninja')
def ninja_form():
    return render_template('add_ninja.html', all_dojos=Dojo.get_all_dojos())