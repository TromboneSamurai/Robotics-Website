from my_app import app
from flask import render_template, request, redirect
import requests
import sys

@app.route("/")
def index():
    return render_template("index.html")
