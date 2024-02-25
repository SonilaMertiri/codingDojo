from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
class Event:
    DB = "forpeopleschema"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id= data['user_id']


    @classmethod
    def create(cls,data):
        query="INSERT INTO events (name, description, user_id) VALUES (%(name)s, %(description)s, %(user_id)s);"
        return connectToMySQL(cls.DB).query_db(query,data)
    

    @classmethod
    def get_all(cls):
        query= "SELECT * FROM events;"
        results= connectToMySQL(cls.DB).query_db(query)
        events=[]
        if results:
            for event in results:
                events.append(event)
        return events
    
    #shikoje me kujdes kete ne kete menyre do shtojme donations
    @classmethod
    def get_event_by_id(cls, data):
        query = "SELECT * FROM events LEFT JOIN users on events.user_id = users.id WHERE events.id = %(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        if result:
            # comments = []

            # query2 = "SELECT * FROM comments left join users on comments.user_id = users.id where comments.book_id = %(id)s;"
            # result2 = connectToMySQL(cls.DB).query_db(query2, data)
            # if result2:
            #     for comment in result2:
            #         comments.append(comment)
            # result[0]['comments'] = comments

            # query3 = "SELECT users.firstName, users.lastName FROM likes left join users on likes.user_id = users.id where likes.book_id = %(id)s;"
            # result3 = connectToMySQL(cls.DB).query_db(query3, data)
            # likes = []
            # if result3:
            #     for like in result3:
            #         likes.append(like)
            # result[0]['likes'] = likes
            return result[0]
        return False
    

    @classmethod
    def deleteEvent(cls,data):
        query="DELETE FROM events WHERE id=%(id)s;"
        return connectToMySQL(cls.DB).query_db(query,data)
    
    @classmethod
    def update(cls,data):
        query="UPDATE events SET name= %(name)s, description= %(description)s WHERE events.id=%(id)s;"
        return connectToMySQL(cls.DB).query_db(query,data)
    

    @staticmethod
    def validate_event(event):
        is_valid= True
        if len(event['name'])<2:
            flash('Name should be more than two characters', 'nameEvent')
            is_valid=False
        if len(event['description'])<10:
            flash('Description should be more than 10 characters', 'descriptionEvent')
            is_valid=False
        return is_valid
    
    @staticmethod
    def validate_event_update(event):
        is_valid= True
        if len(event['name'])<2:
            flash('Name should be more than two characters', 'nameEvent')
            is_valid=False
        if len(event['description'])<10:
            flash('Description should be more than 10 characters', 'descriptionEvent')
            is_valid=False
        return is_valid