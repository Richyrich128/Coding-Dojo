from band_app.config.mysqlconnection import connectToMySQL
from band_app.controllers import dojos, ninjas
from band_app import app
if __name__=="__main__":
    app.run(debug=True)