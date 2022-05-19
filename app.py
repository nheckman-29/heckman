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


@app.route("/", methods=["GET", "POST"])
def initial():
    """
    Initial Site Landing Page
    """
    return render_template("index.html")


app.run(
    host=os.getenv("IP", "0.0.0.0"), 
    port=os.getenv("PORT", "8080"), 
    debug=True
)
