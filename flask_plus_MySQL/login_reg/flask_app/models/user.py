import re
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app) 

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
    
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('login_reg_schema').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email, password) VALUES ( %(first_name)s , %(last_name)s , %(email)s , %(password)s);"
        return connectToMySQL('login_reg_schema').query_db( query, data )


    @staticmethod
    def validate_registration(user):
        is_valid = True 
        if len(user['first_name']) < 2:
            flash("First name must be at least 2 characters.")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last name must be at least 2 characters.")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Email cannot be blank!", 'email')
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False
        if len(user['confirm_password']) < 8:
            flash("Doesnt match the password above.")
            is_valid = False
        return is_valid

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("login_reg_schema").query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])


    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"

        result = connectToMySQL('login_reg_schema').query_db( query, data )
        return cls(result[0])

    # @classmethod
    # def update(cls,data):
    #     query = "UPDATE users SET first_name = %(first_name)s, last_name =%(last_name)s, email =  %(email)s, updated_at=NOW()  WHERE id = %(id)s;"
    #     return connectToMySQL('login_reg_schema').query_db( query, data )

    # @classmethod
    # def destroy(cls,data):
    #     query = "DELETE FROM users WHERE id = %(id)s;"
    #     return connectToMySQL('login_reg_schema').query_db( query, data )



