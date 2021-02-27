#Import all required extensions for app to run
import json
from flask_pymongo import PyMongo
from flask import Flask, jsonify, render_template, redirect
from bson.json_util import dumps
from pymongo import MongoClient

app = Flask(__name__)

#Provide a route to the page that is presented when app is initially run 
@app.route("/")
def home():
    #GoTo webpage
    return render_template("Homepage.html")

if __name__ == "__main__":
    app.run(debug=True)