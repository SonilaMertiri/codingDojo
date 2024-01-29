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
        'id':id
    }
    book= Book.get_book_by_id(data)
    if book:
        return render_template('one_book.html', book=book)
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
