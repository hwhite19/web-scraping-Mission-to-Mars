# MongoDB and Flask Application

# Dependencies and Setup
from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrape_mars
#import Mission_to_Mars.scrape_mars as scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
# client = pymongo.MongoClient('mongodb://localhost:27017')
# db = client.mars_db
# collection = db.mars

# PyMongo Connection Setup
#################################################
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Route to render index.html template using data from Mongo
# @app.route('/')
# def index():
# 	mars = collection.find_one()
# 	return render_template('index.html', mars=mars)

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrapper():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape_all()
    mars.update({}, mars_data, upsert=True)
    return "Scraping Successful"

# @app.route('/scrape')
# def scrape():
# 	scrape_mars.scrape()
# 	return redirect('/', code = 302)

 


if __name__ == "__main__":
    app.run(debug=True)







# # Flask Setup

# app = Flask(__name__)

# # PyMongo Connection Setup

# app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
# mongo = PyMongo(app)

# # Flask Routes

# # Root Route to Query MongoDB & Pass Mars Data Into HTML Template: index.html to Display Data
# @app.route("/")
# def index():
#     mars = mongo.db.mars.find_one()
#     return render_template("index.html", mars=mars)

# # Scrape Route to Import `scrape_mars.py` Script & Call `scrape` Function
# @app.route("/scrape")
# def scrapper():
#     mars = mongo.db.mars
#     mars_data = scrape_mars.scrape_all()
#     mars.update({}, mars_data, upsert=True)
#     return "Scraping Successful"

# # Define Main Behavior
# if __name__ == "__main__":
#     app.run()