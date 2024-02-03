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
        query="INSERT INTO books(title, description, nr_of_pages, price, author, user_id) VALUES (%(title)s, %(description)s, %(nr_of_pages)s, %(price)s, %(author)s, %(user_id)s);"
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
    def get_book_by_id(cls, data):
        query = "SELECT * FROM books LEFT JOIN users on books.user_id = users.id WHERE books.id = %(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        if result:
            comments = []

            query2 = "SELECT * FROM comments left join users on comments.user_id = users.id where comments.book_id = %(id)s;"
            result2 = connectToMySQL(cls.DB).query_db(query2, data)
            if result2:
                for comment in result2:
                    comments.append(comment)
            result[0]['comments'] = comments

            query3 = "SELECT users.firstName, users.lastName FROM likes left join users on likes.user_id = users.id where likes.book_id = %(id)s;"
            result3 = connectToMySQL(cls.DB).query_db(query3, data)
            likes = []
            if result3:
                for like in result3:
                    likes.append(like)
            result[0]['likes'] = likes
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

    #funksionaliteti per commentet
    @classmethod
    def add_comment(cls,data):
        query='INSERT INTO comments (comment, user_id, book_id) VALUES (%(comment)s, %(user_id)s, %(book_id)s);'
        return connectToMySQL(cls.DB).query_db(query,data)
    
    # por qe te marr te dhenat e userit ose librit ne front duhet te shoh te metoda get_book_by_id aty duhet te bej ndryshime qe te aksesoj disa te dhena
    # bej nje liste boshe per commentet dhe duhet te bejme nje query tjeter query2 qe te marrim kush e krijoj commentin
    @classmethod
    def get_comment_by_id(cls,data):
        query= 'SELECT* FROM comments WHERE comments.id=%(id)s;'
        results= connectToMySQL(cls.DB).query_db(query,data)
        if results:
            return results[0]
        return False
    
    @classmethod
    def updateComment(cls,data):
        query='UPDATE comments SET comment=%(comment)s WHERE id=%(id)s;'
        return connectToMySQL(cls.DB).query_db(query,data)
    
    @classmethod
    def deleteComment(cls,data):
        query='DELETE FROM comments WHERE id=%(id)s;'
        return connectToMySQL(cls.DB).query_db(query,data)
    
    # the methods for likes, you have changes in get book by id method too to add the likes, there is a third query, and some changes in front end as well at one_book.html
    @classmethod
    def addLike(cls, data):
        query = "INSERT INTO likes (user_id, book_id) VALUES (%(user_id)s, %(book_id)s);"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def removeLike(cls, data):
        query = "DELETE FROM likes WHERE book_id=%(book_id)s AND user_id = %(user_id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def get_users_who_liked_by_book_id(cls, data):
        query ="SELECT user_id FROM likes where book_id = %(book_id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        usersId = []
        if results:
            for userId in results:
                usersId.append(userId['user_id'])
        return usersId


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
    

    @classmethod
    def delete_all_book_comments(cls, data):
        query ="DELETE FROM comments where comments.book_id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)