from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User

class Show:
    DB = "mylastdb"
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.network = data['network']
        self.comments = data['comments']
        self.release_date= data['release_date']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user= data['user']



    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM shows LEFT JOIN users ON shows.user_id = users.id;'
        results = connectToMySQL(cls.DB).query_db(query)
        all_shows = []
        for result in results:
            show_user = User({
                'id': result['user_id'],
                'email': result['email'],
                'first_name': result['first_name'],
                'last_name': result['last_name'],
                'created_at': result['users.created_at'],
                'updated_at': result['users.updated_at'],
                'password': result['password'],
                'confirm_password': result['confirm_password']
            })
            new_show = Show({
                'id': result['id'],
                'title': result['title'],
                'network': result['network'],
                'release_date': result['release_date'],
                'comments': result['comments'],
                'created_at': result['created_at'],
                'updated_at': result['updated_at'],
                'user': show_user
            })
            all_shows.append(new_show)
        return all_shows


    @classmethod
    def save(cls,data):
        query='INSERT INTO shows (title, network, release_date, comments, user_id) values (%(title)s, %(network)s, %(release_date)s, %(comments)s, %(user_id)s);'
        result= connectToMySQL(cls.DB).query_db(query,data)
        return result
    
    @classmethod
    def get_shows_by_id(cls,data):
        query="SELECT * FROM shows LEFT JOIN users ON shows.user_id=users.id WHERE shows.id=%(id)s;"
        result= connectToMySQL(cls.DB).query_db(query,data)
        if result:
            commentss = []

            query2 = "SELECT * FROM commentss left join users on commentss.user_id = users.id where commentss.show_id = %(id)s;"
            result2 = connectToMySQL(cls.DB).query_db(query2, data)
            if result2:
                for comment in result2:
                    commentss.append(comment)
            result[0]['commentss'] = commentss
            return result[0]
        return False
    
    @classmethod
    def update(cls,data):
        query="UPDATE shows SET title=%(title)s, network= %(network)s, comments= %(comments)s, release_date= %(release_date)s WHERE shows.id=%(id)s;"
        return connectToMySQL(cls.DB).query_db(query,data)
    
    @classmethod
    def deleteShow(cls,data):
        query="DELETE FROM shows WHERE id=%(id)s;"
        return connectToMySQL(cls.DB).query_db(query,data)
    

    # metoda per comments
    @classmethod
    def add_comment(cls,data):
        query='INSERT INTO commentss (comment, user_id, show_id) VALUES (%(comment)s, %(user_id)s, %(show_id)s);'
        return connectToMySQL(cls.DB).query_db(query,data)
    
    @classmethod
    def get_comment_by_id(cls,data):
        query= 'SELECT* FROM commentss WHERE comments.id=%(id)s;'
        results= connectToMySQL(cls.DB).query_db(query,data)
        if results:
            return results[0]
        return False
    
    @classmethod
    def deleteComment(cls,data):
        query='DELETE FROM commentss WHERE id=%(id)s;'
        return connectToMySQL(cls.DB).query_db(query,data)

    @staticmethod
    def validate_show_content(show):
        is_valid= True
        if len(show['title'])<3:
            flash('Recipe name must be at least 3 characters', 'titleShow')
            is_valid=False
        if len(show['network'])<3:
            flash('You should put a valid description for recipe', 'networkShow')
            is_valid=False
        if len(show['comments'])<3:
            flash('Involve some instructions for your recipe', 'commentsShow')
            is_valid=False
        return is_valid
    
