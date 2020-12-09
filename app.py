import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("landing-page.html")


@app.route("/srd_lookup")
def srd_lookup():
    return render_template("srd-lookup.html")


@app.route("/dwarf_lookup")
def dwarf_lookup():
    return render_template("srd-lookup.html",
                           races=mongo.db.races.find(
                            {"name": "Dwarf"}))


@app.route("/halfling-lookup")
def halfling_lookup():
    return render_template("srd-lookup.html",
                           races=mongo.db.races.find(
                            {"name": "Halfling"}))


@app.route("/dragonborn-lookup")
def dragonborn_lookup():
    return render_template("srd-lookup.html",
                           races=mongo.db.races.find(
                            {"name": "Dragonborn"}))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
