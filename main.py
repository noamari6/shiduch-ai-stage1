from flask import Flask, request, render_template
import os

app = Flask(__name__)

profiles = []

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        full_name = request.form["full_name"]
        age = request.form["age"]
        city = request.form["city"]
        religious_level = request.form["religious_level"]
        about = request.form["about"]

        profile = {
            "full_name": full_name,
            "age": age,
            "city": city,
            "religious_level": religious_level,
            "about": about
        }

        profiles.append(profile)
        return render_template("profiles.html", profiles=profiles)

    return render_template
