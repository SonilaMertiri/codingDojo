from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.show import Show
from flask_app.models.user import User



@app.route('/create/show')
def addShow():
    if 'user_id' in session:
        return render_template('createShow.html')
    return redirect('/')


@app.route('/create/show', methods=['POST'])
def create_show():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'title': request.form['title'],
        'network': request.form['network'],
        'release_date': request.form['release_date'],
        'comments': request.form['comments'],
        'user_id':session['user_id']
    }

    is_valid=Show.validate_show_content(data)
    if  is_valid:
        Show.save(data)
        return redirect('/')
    return redirect(request.referrer)


@app.route('/shows/details/<int:id>')
def show_details(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': id
    }
    show = Show.get_shows_by_id(data)
    user_id = show['user_id']  
    user = User.get_user_by_id(user_id)  
    if show:
        return render_template('showDetails.html', show=show, user=user)
    return redirect('/')



@app.route('/update/show/<int:id>')
def edit_show(id):
    if 'user_id' not in session:
        return redirect('/')
    data={
        'id':id
    }
    show= Show.get_shows_by_id(data)
    if show and show['user_id']== session['user_id']:
        return render_template('editShow.html', show=show)
    return redirect('/')

@app.route('/update/show/<int:id>', methods=['POST'])
def update_show(id):
    if 'user_id' not in session:
        return redirect('/')
    data={
        'id':id
    }
    show= Show.get_shows_by_id(data)
    if show and show['user_id']== session['user_id']:
        data = {
            'title': request.form['title'],
            'network': request.form['network'],
            'release_date': request.form['release_date'],
            'comments': request.form['comments'],
            'id': id
        }
        is_valid= Show.validate_show_content(data)
        if is_valid:
            Show.update(data)
            return redirect('/')
        # return redirect('/shows/' + str(id))
    return redirect(request.referrer)

@app.route('/shows/delete/<int:id>')
def delete_show(id):
    if 'user_id' not in session:
        return redirect('/')
    data={
        'id': id
    }
    recipe= Show.get_shows_by_id(data)
    if recipe['user_id']== session['user_id']:
        Show.deleteShow(data)
    return redirect('/')


@app.route('/add/comment/<int:id>', methods=['POST'])
def addComment(id):
    if 'user_id' not in session:
        return redirect('/')
    if len(request.form['comment'])<2:
        flash('The comment should be at least two characters', 'comment')
        return redirect(request.referrer)
    data={
        'comment': request.form['comment'],
        'user_id': session['user_id'],
        'show_id': id
    }
    Show.add_comment(data)
    return redirect(request.referrer)

@app.route('/delete/comment/<int:id>')
def deleteComment(id):
    if 'user_id' not in session:
        return redirect('/')
    data={
        'id':id
    }
    komenti=Show.get_comment_by_id(data)
    if komenti['user_id']== session['user_id']:
        Show.deleteComment(data)
    return redirect(request.referrer)