from flask import Flask, render_template, redirect, request
# import the class from friend.py
from user import User
app = Flask(__name__)


@app.route("/")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    print(users)
    return render_template("index.html", all_users= users)


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
            
if __name__ == "__main__":
    app.run(debug=True)