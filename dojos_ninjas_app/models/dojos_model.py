from dojos_ninjas_app.config.mysqlconnection import connectToMySQL
from dojos_ninjas_app import DATABASE 
#need to add this in order to create instances of this class Ninja
from dojos_ninjas_app.models.ninjas_model import Ninja


class Dojo:
        ## must match sql table
    def __init__(self, data):
        self.id = data['id']
        self.dojo_name = data['dojo_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        result = connectToMySQL(DATABASE).query_db(query)
        if result:
            ## setting all_dojos as an empty list 
            all_dojos = []
            ## looping through the results and appending with the constructor of instance, dojo will represent each row in our database table. Creating an instance for every row from our database
            for dojo in result:
                all_dojos.append(cls(dojo))
            return all_dojos
        return []

    ## creating dojo inserting into dojo table
    @classmethod 
    def create(cls, data):
        query = "INSERT INTO dojos (dojo_name) VALUES (%(dojo_name)s);"
        return connectToMySQL(DATABASE).query_db(query, data)


    
    @classmethod
    ## need to add data because there is a where statement in my query
    def get_all_ninjas(cls, data):
    ## returning dojos and ninjas with join to display dojos with their ninjas
        query = "SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)

        if result:
            #adding new_dojo as instance, grabbing first element in the list, only need to do it once because all elements have the the dojo information because it is accessing the dojo table in our database
            new_dojo = cls(result[0])
            ## creating empty list to loop through and add ninja to particular dojo
            ninjas_list = []
            for row in result:
            ## loop through the entire list to create the ninja instances, this is why we imported the Ninja model at the top of the page
                one_ninja = {
                    'id' : row['ninjas.id'],
                    'first_name' : row['first_name'],
                    'last_name' : row['last_name'],
                    'age': row['age'],
                    'created_at' : row['created_at'],
                    'updated_at' : row['updated_at'],
                    'dojo_id' : row['dojo_id'],
                }
                ninja = Ninja(one_ninja)
                # adding attribute ninjas_list just for this instance that will be returned
                ninjas_list.append(ninja)
                #creating instance new_dojo connecting to other table as a list, will be sent to controller and that is then sent to the template
            new_dojo.ninjas_list = ninjas_list
            return new_dojo
        return []