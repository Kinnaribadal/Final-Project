#Import all required extensions for app to run
import json
from flask_pymongo import PyMongo
from flask import Flask, jsonify, render_template, redirect
from bson.json_util import dumps
from pymongo import MongoClient

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)