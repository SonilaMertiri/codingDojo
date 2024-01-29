from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    DB= "dojos_and_ninjas_schema"
    def __init__(self, db_data ):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        # We create a list so that later we can add in all the ninjass that are associated with a dojo.
        self.ninjas = []

    #kjo eshte per te marre gjithe dojot
    @classmethod
    def get_all_dojos(cls):
        query= "SELECT * FROM dojos;"
        results = connectToMySQL(cls.DB).query_db(query)
        all_dojos=[]
        for dojo in results:
            all_dojos.append(cls(dojo))
        return all_dojos
    
    #ketu ben insert nje dojo te ri ne databaze
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL(cls.DB).query_db( query, data)

    @classmethod
    def get_dojo_with_ninjas(cls, data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        # results will be a list of topping objects with the ninja attached to each row. 
        dojos=[]
        if results:
            for row in results:
                dojos.append(row)
        return dojos
