from dojos_ninjas_app.config.mysqlconnection import connectToMySQL
from dojos_ninjas_app import DATABASE

class Ninja:
        ## must match sql table
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        ## Class method required because a query is being executed
    @classmethod 
    def create(cls, data):
        query = "INSERT INTO ninjas(dojo_id, first_name, last_name, age) VALUES ( %(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s );"
        
        return connectToMySQL(DATABASE).query_db(query, data)
        

