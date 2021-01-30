import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
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


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}!".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/", methods=["GET", "POST"])
def profile():
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    quests = list(mongo.db.quests.find())
    characters = list(mongo.db.characters.find())

    if session["user"]:
        return render_template(
            "profile.html", quests=quests,
            username=username, characters=characters)
    return redirect(url_for("login"))


# LOGOUT
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out. Come back soon!")
    session.pop("user")
    return redirect(url_for("login"))


# PAGE TO DELETE USERS ACCOUNT FROM DB
@app.route("/account/delete", methods=["GET", "POST"])
def delete_account():
    if session.get('user'):
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

        return render_template("delete_account.html", username=username)

    return redirect(url_for("login"))


# PAGE TO CONFIRM ACCOUNT DELETION FROM DB
@app.route("/account/delete-confirm", methods=["GET", "POST"])
def delete_account_confirm():
    mongo.db.users.remove({"username": session["user"]})
    flash("User Deleted")
    session.pop("user")
    return redirect(url_for("register"))


# ADD/EDIT/DELETE QUEST ROUTES
@app.route("/quest/add", methods=["GET", "POST"])
def add_quest():
    if request.method == "POST":
        quest = {
            "quest_name": request.form.get("quest_name"),
            "quest_description": request.form.get("quest_description"),
            "quest_rewards": request.form.get("quest_rewards"),
            "created_by": session["user"]
        }
        mongo.db.quests.insert_one(quest)
        flash("Task Successfully Added!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("profile", username=session["user"])


@app.route("/quest/<quest_id>/edit", methods=["GET", "POST"])
def edit_quest(quest_id):
    if request.method == "POST":
        quest = {
            "quest_name": request.form.get("quest_name"),
            "quest_description": request.form.get("quest_description"),
            "quest_rewards": request.form.get("quest_rewards"),
            "created_by": session["user"]
        }
        mongo.db.quests.update({"_id": ObjectId(quest_id)}, quest)
        flash("Quest Successfully Updated!")

    quest = mongo.db.quests.find_one({"_id": ObjectId(quest_id)})
    return redirect(url_for("profile", username=session["user"]))


@app.route("/quest/<quest_id>/delete")
def delete_quest(quest_id):
    mongo.db.quests.remove({"_id": ObjectId(quest_id)})
    flash("Quest Successfully Deleted!")
    return redirect(url_for("profile", username=session["user"]))


# CHARACTER ADD
@app.route("/character/add", methods=["GET", "POST"])
def add_character():
    if request.method == "POST":
        character = {
            "character_avatar": request.form.get("character_avatar"),
            "character_name": request.form.get("character_name"),
            "character_race": request.form.get("character_race"),
            "character_class": request.form.get("character_class"),
            "character_level": request.form.get("character_level"),
            "character_alignment": request.form.get("character_alignment"),
            "character_ac": request.form.get("character_ac"),
            "character_hp": request.form.get("character_hp"),
            "character_str": request.form.get("character_str"),
            "character_int": request.form.get("character_int"),
            "character_dex": request.form.get("character_dex"),
            "character_wis": request.form.get("character_wis"),
            "character_con": request.form.get("character_con"),
            "character_cha": request.form.get("character_cha"),
            "created_by": session["user"]
        }
        mongo.db.characters.insert_one(character)
        flash("Character Successfully Added!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("profile", username=session["user"])


@app.route("/character/<character_id>/edit", methods=["GET", "POST"])
def edit_character(character_id):
    if request.method == "POST":
        character = {
            "character_avatar": request.form.get("character_avatar"),
            "character_name": request.form.get("character_name"),
            "character_race": request.form.get("character_race"),
            "character_class": request.form.get("character_class"),
            "character_level": request.form.get("character_level"),
            "character_alignment": request.form.get("character_alignment"),
            "character_ac": request.form.get("character_ac"),
            "character_hp": request.form.get("character_hp"),
            "character_str": request.form.get("character_str"),
            "character_int": request.form.get("character_int"),
            "character_dex": request.form.get("character_dex"),
            "character_wis": request.form.get("character_wis"),
            "character_con": request.form.get("character_con"),
            "character_cha": request.form.get("character_cha"),
            "created_by": session["user"]
        }
        mongo.db.characters.update({"_id": ObjectId(character_id)}, character)
        flash("Character Successfully Updated!")

    character = mongo.db.characters.find_one({"_id": ObjectId(character_id)})
    return redirect(url_for("profile", username=session["user"]))


@app.route("/character/<character_id>/delete")
def delete_character(character_id):
    mongo.db.characters.remove({"_id": ObjectId(character_id)})
    flash("Character Successfully Deleted!")
    return redirect(url_for("profile", username=session["user"]))


# LOOKUP HOME ROUTE
@app.route("/lookup")
def lookup():
    return render_template("lookup.html")


# ROUTES FOR DB COLLECTIONS
@app.route("/race_lookup")
def race_lookup():
    race_name = request.args.get('name')
    races = mongo.db.races.find({"name": race_name})
    return render_template("lookup.html",
                           races=races)


@app.route("/class_lookup")
def class_lookup():
    class_name = request.args.get('name')
    classes = mongo.db.classes.find({"name": class_name})
    return render_template("lookup.html",
                           classes=classes)


@app.route("/spell_lookup")
def spell_lookup():
    spell_name = request.args.get('name')
    spells = mongo.db.spells.find({"name": spell_name})
    return render_template("lookup.html",
                           spells=spells)


@app.route("/article_lookup")
def article_lookup():
    article_name = request.args.get('name')
    return render_template(article_name + ".html")


@app.route("/resources")
def resources():
    books = list(mongo.db.books.find())
    return render_template("resources.html", books=books)


# ERROR 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.route("/legal")
def legal():
    return render_template("legal.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
