"""
Nathan Heckman Career Resume Site
"""

import os
from flask import Flask, session, abort, redirect, render_template
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

@app.route("/")
def initial():
    return redirect("/home")


@app.route("/home", methods=["GET", "POST"])
def home():
    """
    Initial Site Landing Page
    """
    return render_template("home.html")

@app.route("/resume", methods=["GET", "POST"])
def resume():
    """
    Resume Preview and Download
    """
    return render_template("resume.html")


@app.route("/projects", methods=["GET", "POST"])
def projects():
    """
    Project Descriptions and Demos/Pictures
    """
    return render_template("projects.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """
    Personal Contact and Email Functionality
    """
    return render_template("contact.html")


app.run(
    host=os.getenv("IP", "0.0.0.0"), 
    port=os.getenv("PORT", "8080"), 
    debug=True
)
