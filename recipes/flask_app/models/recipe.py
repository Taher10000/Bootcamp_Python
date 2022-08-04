from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask import flash


class Recipe:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.thirty_min = data['thirty_min']
        self.instructions = data['instructions']
        self.date_cooked = data['date_cooked']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users = []

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO recipes (name, description, thirty_min, instructions, date_cooked, created_at, updated_at, user_id) VALUES ( %(name)s ,%(description)s, %(thirty_min)s, %(instructions)s, %(date_cooked)s, NOW(), NOW(), %(user_id)s);"
        return connectToMySQL('recipes_schema').query_db( query, data )

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL('recipes_schema').query_db(query)
        recipes = []
        for recipe in results:
            recipes.append( cls(recipe) )
        return recipes
    
    @classmethod
    def get_from_id(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL('recipes_schema').query_db(query, data)
        print(results[0])
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"

        result = connectToMySQL('recipes_schema').query_db( query, data )
        return cls(result[0])

    @classmethod
    def get_from_user_id(cls, data):
        query = "SELECT * FROM recipes WHERE user_id = %(user_id)s;"
        results = connectToMySQL('recipes_schema').query_db(query, data)
        all_recipes = []
        for row in results:
            all_recipes.append(cls(row))
        return all_recipes

    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, date_cooked = %(date_cooked)s, instructions = %(instructions)s, user_id = %(user_id)s WHERE id = %(id)s;"
        return connectToMySQL('recipes_schema').query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL('recipes_schema').query_db(query, data)
    
    @classmethod
    def get_all_with_recipe(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;" 
        results = connectToMySQL('recipes_schema').query_db(query)
        list_recipes = []
        print(results)
        for row in results:
            current_recipe = cls(row)
            user_data = {
                **row,
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at'],
                "id": row['users.id']
            }
            current_user = User(user_data)
            current_recipe.user = current_user
            list_recipes.append(current_recipe)
        return list_recipes


    @staticmethod
    def validate_recipe(data):
        is_valid = True 
        if data['name'] == "":
            flash("Name must not be empty!")
            is_valid = False
        if data['description'] == "":
            flash("Description must not be empty!")
            is_valid = False
        if data['date_cooked'] == "":
            flash("Date must not be empty!")
            is_valid = False
        if data['instructions'] == "":
            flash("Instructions must not be empty!")
            is_valid = False
        return is_valid

        





