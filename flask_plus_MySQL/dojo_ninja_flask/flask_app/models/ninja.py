from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls, data ):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ( %(first_name)s ,%(last_name)s ,%(age)s, %(dojo_id)s);"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data )
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas

    # @classmethod
    # def get_dojo_with_ninjas( cls , data ):
    #     query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = ninjas.id WHERE dojos.id = %(id)s;"
    #     results = connectToMySQL('dojos_and_ninjas_schema').query_db( query , data )
    #     dojo = cls( results[0] )
    #     for row_from_db in results:
    #         # Now we parse the burger data to make instances of burgers and add them into our list.
    #         ninja_data = {
    #             "id" : row_from_db["ninjas.id"],
    #             "first_name" : row_from_db["ninjas.first_name"],
    #             "last_name" : row_from_db["ninjas.last_name"],
    #             "age" : row_from_db["ninjas.age"],
    #             "created_at" : row_from_db["ninjas.created_at"],
    #             "updated_at" : row_from_db["ninjas.updated_at"]
    #         }
    #         dojo.ninjas.append( ninja.Ninja( ninja_data ) )
    #     return dojo

    # @classmethod
    # def get_one(cls,data):
    #     query = "SELECT * FROM users WHERE id = %(id)s;"

    #     result = connectToMySQL('users_schema').query_db( query, data )
    #     return cls(result[0])

    # @classmethod
    # def update(cls,data):
    #     query = "UPDATE users SET first_name = %(first_name)s, last_name =%(last_name)s, email =  %(email)s, updated_at=NOW()  WHERE id = %(id)s;"
    #     return connectToMySQL('users_schema').query_db( query, data )

    # @classmethod
    # def destroy(cls,data):
    #     query = "DELETE FROM users WHERE id = %(id)s;"
    #     return connectToMySQL('users_schema').query_db( query, data )



