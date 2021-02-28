#Import all required extensions for app to run
import json
from flask_pymongo import PyMongo
from flask import Flask, jsonify, render_template, request, redirect
from bson.json_util import dumps
from pymongo import MongoClient
from joblib import load

app = Flask(__name__)

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
@app.route("/Results.html")
def results_page():
    #GoTo webpage
    return render_template("Results.html")

#Provide a route that will outsorce our mongodb data as an API to our webpages
#NOT CREATED YET
@app.route("/our-data-api")
def scrape():
    #Set variable to hold what is returned from calling the function
    pipeline = load("Resources/random_forest.joblib")
    #Jsonify the query 
    return pipeline
    
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