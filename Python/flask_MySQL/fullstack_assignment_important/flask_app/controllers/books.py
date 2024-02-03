from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.book import Book

@app.route('/books')
def books():
    if 'user_id' in session:
        books= Book.get_all()
        return render_template('books.html', books=books)
    return redirect('/')

@app.route('/books/new')
def addBook():
    if 'user_id' in session:
        return render_template('addBook.html')
    return redirect('/')

@app.route('/books/new', methods=['POST'])
def addNewBook():
    if 'user_id' not in session:
        return redirect('/')
    if not Book.validate_book(request.form):
        return redirect(request.referrer)
    #kjo me larte eshte logjika e validimeve, tani ndertojme logjiken pas validimeve
    #me poshte ruajme te dhenat
    data={
        'title': request.form['title'],
        'description':request.form['description'],
        'nr_of_pages':request.form['nr_of_pages'],
        'price':request.form['price'],
        'author':request.form['author'],
        'user_id':session['user_id']
    }
    Book.create(data)
    return redirect('/')


@app.route('/book/<int:id>')
def view_book(id):
    if 'user_id' not in session:
        return redirect('/')
    data={
        'id':id,
        'book_id': id
    }
    book= Book.get_book_by_id(data)
    if book:
        usersWhoLikes = Book.get_users_who_liked_by_book_id(data)
        return render_template('one_book.html', book=book, usersWhoLikes= usersWhoLikes)
    return redirect('/')

@app.route('/book/delete/<int:id>')
def delete_book(id):
    if 'user_id' not in session:
        return redirect('/')
    data={
        'id': id
    }
    book= Book.get_book_by_id(data)
    if book['user_id']== session['user_id']:
        Book.delete_all_book_comments(data)
        Book.deleteBook(data)
    return redirect('/')


# duhet te vendosim nje kusht te controlleri pervec id bej eshe nje get book by id sepse dikush qe mund te hamendesoj routin mund te bej delete edhe pse mund te mos jete krijuesi

@app.route('/book/edit/<int:id>')
def edit_book(id):
    if 'user_id' not in session:
        return redirect('/')
    data={
        'id':id
    }
    book= Book.get_book_by_id(data)
    if book and book['user_id']== session['user_id']:
        return render_template('edit_book.html', book=book)
    return redirect('/')

@app.route('/book/update/<int:id>', methods=['POST'])
def update_book(id):
    if 'user_id' not in session:
        return redirect('/')
    data={
        'id':id
    }
    book= Book.get_book_by_id(data)
    if book and book['user_id']== session['user_id']:
        if not Book.validate_book_update(request.form):
            return redirect(request.referrer)
        data={
            'description':request.form['description'],
            'nr_of_pages':request.form['nr_of_pages'],
            'price':request.form['price'],
            'id': id
        }
        Book.update(data)
        return redirect('/book/' +str(id))
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
        'book_id': id
    }
    Book.add_comment(data)
    return redirect(request.referrer)


@app.route('/edit/comment/<int:id>')
def editComment(id):
    if 'user_id' not in session:
        return redirect('/')
    data={
        'id':id
    }
    commenti=Book.get_comment_by_id(data)
    if commenti['user_id']== session['user_id']:
        return render_template('editComment.html', commenti=commenti)
    return redirect('/')

@app.route('/edit/comment/<int:id>', methods=['POST'])
def updateComment(id):
    if 'user_id' not in session:
        return redirect('/')
    if len(request.form['comment'])<2:
        flash('The comment should be at least two characters', 'comment')
        return redirect(request.referrer)
    data={
        'comment': request.form['comment'],
        'id':id
    }
    komenti=Book.get_comment_by_id(data)
    if komenti['user_id']== session['user_id']:
        Book.updateComment(data)
    return redirect('/book/'+ str(komenti['book_id']))

@app.route('/delete/comment/<int:id>')
def deleteComment(id):
    if 'user_id' not in session:
        return redirect('/')
    data={
        'id':id
    }
    komenti=Book.get_comment_by_id(data)
    if komenti['user_id']== session['user_id']:
        Book.deleteComment(data)
    return redirect(request.referrer)

#the routes for likes
@app.route('/add/like/<int:id>')
def addLike(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'book_id': id,
        'user_id': session['user_id']
    }
    usersWhoLikes = Book.get_users_who_liked_by_book_id(data)
    print(usersWhoLikes)
    if session['user_id'] not in usersWhoLikes:
        Book.addLike(data)
    return redirect(request.referrer)

@app.route('/remove/like/<int:id>')
def removeLike(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'book_id': id,
        'user_id': session['user_id']
    }
    Book.removeLike(data)
    return redirect(request.referrer)