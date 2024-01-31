from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models.user import User
from flask_app.models.post import Post


@app.route('/welcome')
def controller():
    if 'user_id' in session:
        user_id=session['user_id']
        user= User.get_user_by_id(user_id) #get user by id method is used at the root route and i use it to access the first and last mname at the wall template (Welcome user.first_name user.last_name)
        if user:
            all_posts= Post.get_all()
            return render_template('wall.html', user=user, all_posts=all_posts)
    return redirect('/')


@app.route('/')
def registration():
    if 'user_id' in session:
        return redirect('/welcome')
    return render_template('register_login.html')


@app.route('/register', methods=['POST'])
def register():
    if 'user_id' in session:
        return redirect('/')
    
    user= User.get_user_by_email(request.form)
    if user:
        flash('This account already exist!', 'emailRegister')
        return redirect(request.referrer)
    
    if User.validate_userRegister(request.form):
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': bcrypt.generate_password_hash(request.form['password']),
            'confirm_password': bcrypt.generate_password_hash(request.form['confirm_password'])
        }
        session['user_id']=User.create(data)
        return redirect('/')
    return redirect('/')
#till now we made all the routs for user registration including validations



@app.route('/login')
def login():
    if 'user_id' in session:
        return redirect('/')
    return render_template('register_login.html')


@app.route('/login', methods=['POST'])
def loginValid():
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
#these are the login routes get and post



@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')




