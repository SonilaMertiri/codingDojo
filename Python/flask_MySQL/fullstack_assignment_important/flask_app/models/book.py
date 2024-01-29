from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
class Book:
    DB = "fullstack_schema"
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.nr_of_pages = data['nr_of_pages']
        self.price = data['price']
        self.author = data['author']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id= data['user_id']

    @classmethod
    def create(cls,data):
        query="INSERT INTO books(title,description, nr_of_pages, price, author, user_id) VALUES (%(title)s, %(description)s, %(nr_of_pages)s, %(price)s, %(author)s, %(user_id)s);"
        return connectToMySQL(cls.DB).query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query= "SELECT * FROM books;"
        results= connectToMySQL(cls.DB).query_db(query)
        books=[]
        if results:
            for book in results:
                books.append(book)
        return books

    @classmethod
    def get_book_by_id(cls,data):
        query="SELECT * FROM books LEFT JOIN users ON books.user_id=users.id WHERE books.id=%(id)s;"
        result= connectToMySQL(cls.DB).query_db(query,data)
        if result:
            return result[0]
        return False
    
    @classmethod
    def deleteBook(cls,data):
        query="DELETE FROM books WHERE id=%(id)s;"
        return connectToMySQL(cls.DB).query_db(query,data)
    
    @classmethod
    def update(cls,data):
        query="UPDATE books SET description= %(description)s, price=%(price)s, nr_of_pages=%(nr_of_pages)s WHERE books.id=%(id)s;"
        return connectToMySQL(cls.DB).query_db(query,data)


    @staticmethod
    def validate_book(book):
        is_valid= True
        if len(book['title'])<2:
            flash('Title should be more than two characters', 'title')
            is_valid=False
        if len(book['description'])<10:
            flash('Description should be more or equal to 10 characters', 'description')
            is_valid=False
        if len(book['nr_of_pages'])<1:
            flash('Number of pages is required', 'nr_of_pages')
            is_valid=False
        if len(book['price'])<1:
            flash('Price is required', 'price')
            is_valid=False
        if len(book['author'])<2:
            flash('Author name is required', 'author')
            is_valid=False
        return is_valid
    
    @staticmethod
    def validate_book_update(book):
        is_valid= True
        if len(book['description'])<10:
            flash('Description should be more or equal to 10 characters', 'description')
            is_valid=False
        if len(book['nr_of_pages'])<1:
            flash('Number of pages is required', 'nr_of_pages')
            is_valid=False
        if len(book['price'])<1:
            flash('Price is required', 'price')
            is_valid=False
        return is_valid
    