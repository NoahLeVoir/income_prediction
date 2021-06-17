# Import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib
from pickle import load


# Placeholder code incase we use a db
# Define the database connection parameters
    # database_name = ''
    # connection_string = f'postgresql://{username}:{password}@localhost:5432/{database_name}'
# Connect to the database
# Import tables


# Instantiate the Flask application
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 # Effectively disables page caching

#load scalers here


### Define app routes ###
#main/home page this will have our ml model analysis
@app.route("/")
def home():
    webpage = render_template("index.html")
    return webpage

#this rought explains where and what dataset we are using for our ml models
@app.route("/about")
def projectOverview():
    webpage = render_template("about.html")
    return webpage

# We might have to move away from making any predcitons 
# might delete this route
# route that takes user input and makes a predictions
@app.route("/predictor",methods=['Get','POST']) #,methods=['POST']
def predictor():
    #income prediction labels
    prediction_labels = [">=50","<=50"]

    # Load the model.
    randomforest = load(open('randomforest.pkl', 'rb'))

    # Load the scaler.
    scaler = load(open('scaler.pkl', 'rb'))

    #these values are from random_forest_ml.ipynb > input_14260,30339,8610 
    prediction1 = [[27,160178,10,0,0,38,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]]
    prediction2 = [[50,175804,13,0,0,40,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]]
    prediction3 = [[24,322931,4,0,1902,40,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]]

    #scaled values
    prediction1_scaled = scaler.transform(prediction1)
    prediction2_scaled = scaler.transform(prediction2)
    prediction3_scaled = scaler.transform(prediction3)
    
    # # need to connect to my buttons for this to work???
    # predict1 = randomforest.predict(prediction1_scaled)
    # print(f'Your income predction is {prediction_labels[predict[0]]}')

    # predict2 = randomforest.predict(prediction2_scaled)
    # print(f'Your income predction is {prediction_labels[predict[0]]}')

    # predict3 = randomforest.predict(prediction3_scaled)
    # print(f'Your income predction is {prediction_labels[predict[0]]}')

    
    webpage = render_template("predictions_model.html",)
    return webpage

#this rought has the about team info
@app.route("/team")
def aboutTeam():
    webpage = render_template("about_us.html")
    return webpage


#  flask requirment to run properly
if __name__ == '__main__':
    app.run(debug=True)