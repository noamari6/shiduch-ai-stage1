from flask import Flask, request, render_template
import os  # צריך בשביל לקרוא את משתנה הסביבה PORT

app = Flask(__name__)

profiles = []

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        full_name = request.form["full_name"]
        age = request.form["age"]
        city = request.form["city"]
        religious_level = request.form["religious_level"]
        about =
