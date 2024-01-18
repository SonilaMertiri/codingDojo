from flask import Flask, render_template, redirect, request, session
import random

app= Flask(__name__)
app.secret_key='cypher pt 2'

@app.route('/')
def index():
    ninja_gold= session.get('gold', 0)
    activities_log= session.get('activities_log', '')
    return render_template('index.html', ninja_gold= ninja_gold, activities_log= activities_log)

@app.route('/process_money', methods=['POST'])
def process_money():
    gold_earned=0
    building = request.form.get('building')

    if building == 'farm':
        gold_earned= random.randint(10,20)

    elif building == 'cave':
        gold_earned= random.randint(5,10)

    elif building == 'house':
        gold_earned= random.randint(2,5)

    elif building == 'casino':
        gold_earned= random.randint(-50,50)

    session['gold']= session.get('gold',0)+ gold_earned

    activity_log= f'Earned {gold_earned} gold at the {building}. \n'
    session['activities_log'] = session.get('activities_log', '') + activity_log

    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset_game():
    session.clear()
    return redirect('/')
    

if __name__ == '__main__':
    app.run(debug=True)
