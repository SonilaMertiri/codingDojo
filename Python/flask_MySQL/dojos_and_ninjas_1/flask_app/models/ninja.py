from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo #ask if you have to import the dojo in here

class Ninja:
    DB= "dojos_and_ninjas_schema"
    def __init__(self, db_data ):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.age = db_data['age']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id ) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        return connectToMySQL(cls.DB).query_db(query, data)