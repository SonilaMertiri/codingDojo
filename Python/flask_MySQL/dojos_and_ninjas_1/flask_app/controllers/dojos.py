from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo

#route per te marr gjithe dojot
@app.route('/')
def add_dojo():
    dojos= Dojo.get_all_dojos()
    return render_template('add_dojo.html', dojos= dojos)

#route per te krijuar nje dojo
@app.route('/add/dojo', methods=['POST'])
def create_dojo():
    data= {
        "name": request.form["name"]
    }
    Dojo.save(data)
    return redirect('/')

@app.route('/ninja/dojo/<int:id>')
def get_dojo_with_ninja(id):
    data={
        'id':id
    }
    ninjas=Dojo.get_dojo_with_ninjas(data)
    return render_template('show_ninjas_of_dojo.html', ninjas=ninjas)