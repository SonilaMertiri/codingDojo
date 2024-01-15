from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        dojo_location = request.form.get('dojolocation')
        favorite_language = request.form.get('favoritelanguage')
        comment = request.form.get('comment')

        return render_template('result.html', name=name, dojo_location=dojo_location, favorite_language=favorite_language, comment=comment)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)