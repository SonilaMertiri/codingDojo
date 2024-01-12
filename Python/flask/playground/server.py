from flask import Flask, render_template
app= Flask(__name__)

@app.route('/play')
def play():
    return render_template('play.html')

@app.route('/play/<int:num>/<color>')
def play_num(num, color):
    return render_template('play_int_color.html', num=num, color=color)

if __name__ == "__main__":
    app.run(debug = True)
