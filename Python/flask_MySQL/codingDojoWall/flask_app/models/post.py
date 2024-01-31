from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User

class Post:
    DB = "logimishembull"
    def __init__(self,data):
        self.id=data['id']
        self.content= data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user= data['user'] #storing the user object and not the id, if we would stoer the id we would do it like that self.user_id= data['user_id'] thats actually how usualy do it


    @classmethod
    def save(cls,data):
        query='INSERT INTO posts (content, user_id) values (%(content)s, %(user_id)s);'
        result= connectToMySQL(cls.DB).query_db(query,data)
        return result
    
    @classmethod
    def delete(cls,post_id):
        query='DELETE from posts WHERE id=%(id)s;'
        data={
            'id': post_id
        }
        return connectToMySQL(cls.DB).query_db(query,data)
    
    @classmethod
    def edit(cls, data):
        query = 'UPDATE posts SET content = %(content)s WHERE id = %(post_id)s;'
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query='SELECT * FROM posts JOIN users ON posts.user_id=users.id ORDER BY posts.created_at DESC;'
        results= connectToMySQL(cls.DB).query_db(query)
        all_posts=[]
        for result in results:
            posting_user=  User({
                'id': result['user_id'],
                'email': result['email'],
                'first_name': result['first_name'],
                'last_name': result['last_name'],
                'created_at': result['users.created_at'],
                'updated_at': result['users.updated_at'],
                'password': result['password'],
                'confirm_password': result['confirm_password']
            })
            new_post= Post({
                'id': result['id'],
                'content': result['content'],
                'created_at': result['created_at'],
                'updated_at': result['updated_at'],
                'user': posting_user
            })
            all_posts.append(new_post)
        return all_posts
    

    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM posts JOIN users ON posts.user_id=users.id WHERE posts.id = %(id)s;'
        result = connectToMySQL(cls.DB).query_db(query, data)
        
        if result:
            post_data = result[0]
            
            posting_user = User({
                'id': post_data['user_id'],
                'email': post_data['email'],
                'first_name': post_data['first_name'],
                'last_name': post_data['last_name'],
                'created_at': post_data['users.created_at'],
                'updated_at': post_data['users.updated_at'],
                'password': post_data['password'],
                'confirm_password': post_data['confirm_password']
            })

            post = Post({
                'id': post_data['id'],
                'content': post_data['content'],
                'created_at': post_data['created_at'],
                'updated_at': post_data['updated_at'],
                'user': posting_user
            })
            return post
        
    @staticmethod
    def validate_post_content(post):
        is_valid=True
        if len(post['content'])<1: #nuk bera fare flash ketu thjesht nese forma do te jete bosh nuk do postohet asgje
            is_valid=False
        return is_valid