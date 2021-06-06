# Import the functions we need from flask
from flask import Flask
from flask import render_template 


# Placeholder code incase we use a db
# Define the database connection parameters
    # database_name = ''
    # connection_string = f'postgresql://{username}:{password}@localhost:5432/{database_name}'
# Connect to the database
# Import tables


# Instantiate the Flask application
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 # Effectively disables page caching

### Define app routes ###
# Index
@app.route("/")
# @app.route("/index.html")
def IndexRoute():
    webpage = render_template("index.html")
    return webpage

@app.route("/about")
def ChartRoute():
    webpage = render_template("about.html", title_we_want="About")
    return webpage

# Other Routes??
# Placeholder for other routes if we want them
@app.route("/???")
def OtherRoutes():



# This statement is required
# Final lines for Flask to run properly
if __name__ == '__main__':
    app.run(debug=True)