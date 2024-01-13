from flask import Flask, render_template
app= Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template('index.html', num=8, another_num=8, color1="red", color2="black")

@app.route('/<int:num>')
def checkerboard_num(num):
    return render_template('index.html', num= num, another_num=8, color1="red", color2="black")

@app.route('/<int:num>/<int:another_num>')
def checkerboard_num_another_num(num, another_num):
    return render_template('index.html', num = num, another_num = another_num, color1="red", color2="black")

@app.route('/<int:num>/<int:another_num>/<string:color1>/<string:color2>')
def checkerboard_color(num, another_num, color1, color2):
    return render_template('index.html', num = num, another_num = another_num, color1=color1, color2=color2)

if __name__== "__main__":
    app.run(debug = True)