from flask_app.config.mysqlconnection import connectToMySQL
# burger.py
from flask_app.models import topping
class Burger:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.bun = data['bun']
        self.meat = data['meat']
        self.calories = data['calories']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        self.toppings = []
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM burgers"
        burgers_from_db = connectToMySQL('burgers').query_db(query)
        burgers = []
        for b in burgers_from_db:
            burgers.append(cls(b))
        return burgers
    # burger.py...
# gets all the burgers and returns them in a list of burger objects .
    @classmethod
    def save(cls,data):
        query = "Insert INTO burgers (name,bun,meat,calories,created_at,updated_at) VALUES(%(name)s,%(bun)s,%(meat)s,%(calories)s,NOW(),NOW());"
        burger_id = connectToMySQL('burgers').query_db(query,data)
        return burger_id
    
    @classmethod
    def get_burger_with_toppings( cls , data ):
        query = "SELECT * FROM burgers LEFT JOIN toppings ON toppings.burger_id = burgers.id WHERE burgers.id = %(id)s;"
        results = connectToMySQL('burgers').query_db( query , data )
        # groups will be a list of music group objects from our raw data
        burger = cls( results[0] )
        for row_from_db in results:
            # Now we parse the topping data to make instances of toppings and add them into our list.
            topping_data = {
                "id" : row_from_db["toppings.id"],
                "topping_name" : row_from_db["topping_name"],
                "created_at" : row_from_db["toppings.created_at"],
                "updated_at" : row_from_db["toppings.updated_at"]
            }
            burger.toppings.append( topping.Topping( topping_data ) )
        return burger