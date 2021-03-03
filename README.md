# Finger on the Pulse
----------------
Members:
Rafael Rodriguez,
Zach Kopec,
Nehemiah Porter,
Kinnari Patel,
Bill Roll 

----------------
# Project Proposal/Topic
GOAL: To Create a website which will help users determine if there’s a chance that the user has an irregular heart beat.

### Data Set

We will be utilizing National Health and Nutrition Examination Survey data from the CDC during 2013 - 2014. This dataset is composed of several health metrics as well as survey data from individuals.

https://www.kaggle.com/cdc/national-health-and-nutrition-examination-survey?select=demographic.csv

# Summary of Steps Taken


### Cleaning Data
* Python (Jupyter Notebook)
  * Pandas (Data Cleaning/Wrangling)
    * Uploaded data via CSV files.
    * Selected necessary columns.
    * Updated/cleaned certain fields to properly use with a machine learning model. 

### Building Model
* SciKit Learn (Machine Learning Model)
  * Model used: RandomForestClassifier
  * Exported model as a joblib file in order to reference while using flask.  

### Loading Data
* MongoDB
  * Load dataset from cleaned CSV data with correct formatting.

### Website Application and build
* Flask
* HTML
* CSS (Bootstrap)
* Javascript
* Website allows for user inputs to be submitted. Model will run and report whether the user is likely to have or not have an irregular heartbeat based on model. 

### Visualizations:
* Matplotlib (Model Visualization within Jupyter Notebook)
* Seaborn (Statistical Analysis- Correlation Matrix)
* Tableau(Data Visulization and Correlation matrix)

----------------
# Visuals
