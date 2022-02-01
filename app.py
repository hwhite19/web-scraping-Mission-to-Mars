from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# use flask pymongo to set up the connection to the database
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_data_db"
mongo = PyMongo(app)

@app.route("/")
def index():
    return "You reached the Index"

@app.route("/scrape")
def scrape():
    marsTable = mongo.db.marsData
    mars_data = scrape_mars.scrape_all()
    marsTable.update_one({}, {"$set": mars_data}, upsert=True)
    #return redirect('/', code=302)
    return mars_data
    # # reference to a database collection (table)
    # marsTable = mongo.db.marsData

    # # drop the table if it exists
    # mongo.db.marsData.drop()

    # # call scrape mars script
    # mars_data = scrape_mars.scrape_all()

    # # take the dictionary and load it into mongoDB
    # marsTable.insert_one(mars_data)

    
if __name__ == "__main__":
    app.run()