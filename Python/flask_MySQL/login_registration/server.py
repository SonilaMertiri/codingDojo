from flask_app import app
#here we import our controllers
from flask_app.controllers import users

if __name__ == "__main__":
    app.run(debug=True, port=8000)