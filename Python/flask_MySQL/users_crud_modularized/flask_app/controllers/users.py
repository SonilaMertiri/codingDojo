from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.user import User


@app.route("/")
def users_data():
    # call the get all classmethod to get all users
    users = User.get_all()
    print(users)
    return render_template("users_data.html", all_users= users)


@app.route('/add_user')
def add_user():
    return render_template('add_user.html')

@app.route('/create_user', methods=['POST'])
def create_user():
    data= {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
    }
    User.save(data)
    return redirect('/')


@app.route('/show_user/<int:user_id>')
def show(user_id):
    # calling the get_one method and supplying it with the id of the user we want to get
    user=User.get_one(user_id)
    return render_template("show_user.html", user=user)

#edit users
@app.route('/edit_user/<int:user_id>')
def edit(user_id):
    user=User.get_one(user_id)
    return render_template('edit_user.html', user=user)

#update the data of the user
@app.route('/update_user/', methods=['POST'])
def update():
    data = {
        "id": request.form["id"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
    }
    User.update(data)
    return redirect('/')

@app.route('/delete_user/<int:user_id>')
def remove_user(user_id):
    data= {
        "id": user_id
    }
    User.remove(data)
    return redirect('/')