from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models.user import User

# ketu krijojme routet per userin

@app.route('/')
def controller():
    if 'user_id' in session:
        return redirect('/books')
    return redirect('/logout')

@app.route('/register')
def registerPage():
    if 'user_id' in session:
        return redirect('/books')
    return render_template('register.html')

# ne kemi nje root books i cili duhet te jete te books.py sepse ne do bejme display books, keshtu qe e krijojme te books
# me poshte do kemi metoden post te registerpage
@app.route('/register', methods=['POST'])
def register():
    if 'user_id' in session:
        return redirect('/')
    if not User.validate_userRegister(request.form):
        return redirect(request.referrer)
    user= User.get_user_by_email(request.form)
    if user:
        flash('This account already exist!', 'emailRegister')
        return redirect(request.referrer)
    data={
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['password'])  #ketu paswordin do e bejme bycrypt per ta ruajtur te enkriptuar
    }
    session['user_id']=User.create(data)
    return redirect('/')


@app.route('/login')
def loginPage():
    if 'user_id' in session:
        return redirect('/books')
    return render_template('login.html')  #kjo te con te faqja e html te forme per tu loguar

#por qe te bejme funksionalitetin e saj na fduhet nje login method POST si me poshte
@app.route('/login', methods=['POST'])
def login():
    if 'user_id' in session:
        return redirect('/')
    if not User.validate_user(request.form):
        return redirect(request.referrer)
    
    user= User.get_user_by_email(request.form)
    if not user:
        flash('This email doesnt exist!', 'emailLogin')
        return redirect(request.referrer)
    
    if not bcrypt.check_password_hash(user['password'], request.form['password']):
        flash('Incorrect password!', 'passwordLogin')
        return redirect(request.referrer)
    
    session['user_id']= user['id']
    return redirect('/')

    #me lart kemi nese useri eshte ne session i bejme redirect te controlleri ne te kundert validojme
    #dhe validimet do ti bejme me nje metode statike ne klasen e user


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

# kemi krijuar routet le te krijojme templatet perkatese per secilen prej tyre

@app.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect('/')
    data={
        'id': session['user_id']
    }
    loggedUser=User.get_user_by_id(data)
    return render_template('profile.html', loggedUser=loggedUser)
    #ndertojme nje metode get user by id njelloj te ngjashme me get user by email vetem se i kalojme id ne kete rast


# bejme routin per editim qe duhet te ket nje get per edit, get-i per edit eshte i njejte me getin per profile, po ashtu edhe routi

@app.route('/edit/user')
def editProfile():
    if 'user_id' not in session:
        return redirect('/')
    data={
        'id': session['user_id']
    }
    loggedUser=User.get_user_by_id(data)
    return render_template('edit_user.html', loggedUser=loggedUser)


@app.route('/edit/user', methods=['POST'])
def edit():
    if 'user_id' not in session:
        return redirect('/')
    if not User.validate_user_update(request.form):
        return redirect(request.referrer)
    data={
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'id': session['user_id']  #id e userit e marrim nga session edhe keshtu nuk eshte e nevojshme ta shenojme te routi
    }
    User.update(data) #duhet krijuar classmethod per User.update te user
    flash('User succesfully updated', 'updateSucces')
    return redirect(request.referrer)

@app.route('/delete/user')
def deleteUser():
    if 'user_id' not in session:
        return redirect('/')
    data={
        'id': session['user_id']
    }
    User.delete(data)
    return redirect('/logout')