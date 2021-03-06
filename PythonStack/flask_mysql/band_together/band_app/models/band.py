# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Band:
    def __init__( self , data ):
        self.id = data['id']
        self.genre = data['genre']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM bands;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        # Create an empty list to append our instances of friends
        dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos ( name , created_at, updated_at ) VALUES ( %(fname)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojos_and_ninjas').query_db( query, data )