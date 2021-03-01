#Import all required extensions for app to run
import json
from flask_pymongo import PyMongo
from flask import Flask, jsonify, render_template, request, redirect
from bson.json_util import dumps
from pymongo import MongoClient
from joblib import load
import numpy as np

app = Flask(__name__)

loaded_model = load("Resources/finalized_model.sav")

#Provide a route to the page that is presented when app is initially run 
@app.route("/")
def home():
    #GoTo webpage
    return render_template("Homepage.html")

#Provide a route to the html process page
@app.route("/Model.html")
def process_page():
    #GoTo webpage
    return render_template("Model.html")

#Provide a route to the html process page
@app.route("/Results.html", methods=['POST', 'GET'])
def results_page():
    #GoTo webpage
    int_features = request.args.get('Age')
    # final_features = [np.array(int_features)]
    # prediction = loaded_model.predict(final_features)

    # output = round(prediction[0], 2)
            
    return render_template("Results.html", prediction_text=int_features)

# #Provide a route that will outsorce our mongodb data as an API to our webpages
# #NOT CREATED YET
# @app.route("/our-data-api")
# def scrape():
#     #Set variable to hold what is returned from calling the function
#     loaded_model = load("Resources/finalized_model.sav")
#     #Jsonify the query 
#     return loaded_model
    
# #function that queries database and returns the data
# def get_data_from_db():
#     client = MongoClient('mongodb://localhost:27017/')
    
#     #Variables for Mongo database and collection
#     db = database.data
#     collection = db.pulse

#     #Query database and put in a list
#     results_dict = list(collection.find({}, {'_id':False}))
#     client.close()

#     #Dictionary is returned from calling function
#     return results_dict


if __name__ == "__main__":
    app.run(debug=True)