from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo'

@app.route('/say/<name>')
def say_name(name):
    return "Hi " + name +"!"

# @app.route('/repeat/<int:num>/<string:name>')
# def repeat_name(num,name):
#     repeated_name= f"{name}<br>" * num
#     return repeated_name

@app.route('/repeat/<int:num>/<text>')
def repeat_text(num,text):
    return render_template('repeat.html', num=num, text=text)


@app.route('/<path:_>')
def make_invalid_route(_):
    return "Sorry! No response. Try again."

if __name__=="__main__":
    app.run(debug=True, host = "localhost")