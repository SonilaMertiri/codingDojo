from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User


class Recipe:
    DB = "logimishembull"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30= data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user= data['user']


    @classmethod
    def get_all(cls):
        query='SELECT * FROM recipes JOIN users ON recipes.user_id=users.id ORDER BY recipes.created_at DESC;'
        results= connectToMySQL(cls.DB).query_db(query)
        all_recipes=[]
        for result in results:
            recipe_user=  User({
                'id': result['user_id'],
                'email': result['email'],
                'first_name': result['first_name'],
                'last_name': result['last_name'],
                'created_at': result['users.created_at'],
                'updated_at': result['users.updated_at'],
                'password': result['password'],
                'confirm_password': result['confirm_password']
            })
            new_recipe= Recipe({
                'id': result['id'],
                'name': result['name'],
                'description': result['description'],
                'instructions': result['instructions'],
                'under_30': result['under_30'],
                'created_at': result['created_at'],
                'updated_at': result['updated_at'],
                'user': recipe_user
            })
            all_recipes.append(new_recipe)
        return all_recipes

    @classmethod
    def save(cls,data):
        query='INSERT INTO recipes (name, description, instructions, under_30, user_id) values (%(name)s, %(description)s, %(instructions)s, %(under_30)s, %(user_id)s);'
        result= connectToMySQL(cls.DB).query_db(query,data)
        return result
    
    @classmethod
    def get_recipe_by_id(cls,data):
        query="SELECT * FROM recipes LEFT JOIN users ON recipes.user_id=users.id WHERE recipes.id=%(id)s;"
        result= connectToMySQL(cls.DB).query_db(query,data)
        if result:
            return result[0]
        return False
    
    @classmethod
    def update(cls,data):
        query="UPDATE recipes SET name=%(name)s, description= %(description)s, instructions= %(instructions)s, under_30=%(under_30)s WHERE recipes.id=%(id)s;"
        return connectToMySQL(cls.DB).query_db(query,data)
    
    @classmethod
    def deleteRecipe(cls,data):
        query="DELETE FROM recipes WHERE id=%(id)s;"
        return connectToMySQL(cls.DB).query_db(query,data)
    
    @staticmethod
    def validate_recipe_content(recipe):
        is_valid= True
        if len(recipe['name'])<3:
            flash('Recipe name must be at least 3 characters', 'nameRecipe')
            is_valid=False
        if len(recipe['description'])<3:
            flash('You should put a valid description for recipe', 'descriptionRecipe')
            is_valid=False
        if len(recipe['instructions'])<3:
            flash('Involve some instructions for your recipe', 'instructionsRecipe')
            is_valid=False
        if recipe['under_30'] not in ('Yes', 'No'):
            flash('Invalid value for "Under 30 minutes"', 'under30Error')
            is_valid = False
        return is_valid
    