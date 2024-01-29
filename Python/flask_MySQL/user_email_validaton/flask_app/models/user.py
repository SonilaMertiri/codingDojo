# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re  # the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

# model the class after the users table from our database
class User:
    DB= "users_schemas"
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.DB).query_db(query)
        # Create an empty list to append our instances of users
        users = []
        # Iterate over the db results and create instances of users with cls.
        for user in results:
            users.append(cls(user))
        return users
    
    #method for create new user        
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"
        result= connectToMySQL(cls.DB).query_db(query, data)
        return result
    
    #method to read the data for one user
    @classmethod
    def get_one(cls, user_id):
        query= "SELECT * FROM users WHERE id= %(id)s;"
        data = {'id': user_id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])
    
    #method to update the data of the user
    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, updated_at= NOW() WHERE id= %(id)s;"
        return connectToMySQL(cls.DB).query_db(query,data)
    

    #method to delete the data of one user by specific id
    @classmethod
    def remove(cls,data):
        query= "DELETE FROM users WHERE id=%(id)s"
        return connectToMySQL(cls.DB).query_db(query,data)
    
    #static method for validations
    @staticmethod
    def validate_user(user):
        is_valid = True # we assume this is true
        if len(user['first_name']) < 3:
            flash("First name is required and it must be more than 3 characters.", 'first_name')
            is_valid = False
        if len(user['last_name']) < 3:
            flash("Last name is required and it must be more than 3 characters.", 'last_name')
            is_valid = False
        if len(user["email"]) <= 0:
            flash("Email is required.", 'email')
            is_valid = False
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!", 'email')
            is_valid = False
        return is_valid
    
            # if len(user["email"]) > 0 and not EMAIL_REGEX.match(user['email']): 
