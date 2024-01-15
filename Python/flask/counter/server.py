from flask import Flask, render_template, session, redirect, request, url_for
app= Flask(__name__)

app.secret_key = 'silver_spoon'


@app.route('/')
def counter_index():
    session['counter']= session.get('counter', 0)+1
    return render_template('index.html', counter= session['counter'])

@app.route('/destroy')
def destroy_session():
    session.clear()
    return redirect(url_for('counter_index'))

@app.route('/increment', methods=['POST'])
def increment_counter():
    session['counter']= session.get('counter',0)+1
    return redirect(url_for('counter_index'))

@app.route('/reset', methods=['POST'])
def reset_counter():
    session['counter']= 0
    return redirect(url_for('counter_index'))

if __name__ == "__main__":
    app.run(debug=True)