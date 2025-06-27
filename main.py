from flask import Flask, request, render_template, redirect, url_for
import os
import base64
import json
from datetime import datetime

app = Flask(__name__)
PROFILE_FILE = "profiles.json"

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        city = request.form.get("city")
        description = request.form.get("description")
        image = request.files["image"]

        if image and image.filename != "":
            image_data = base64.b64encode(image.read()).decode("utf-8")
        else:
            image_data = ""

        profile = {
            "name": name,
            "age": age,
            "city": city,
            "description": description,
            "image": image_data,
            "timestamp": datetime.now().isoformat()
        }

        profiles = []
        if os.path.exists(PROFILE_FILE):
            with open(PROFILE_FILE, "r", encoding="utf-8") as f:
                profiles = json.load(f)

        profiles.append(profile)

        with open(PROFILE_FILE, "w", encoding="utf-8") as f:
            json.dump(profiles, f, ensure_ascii=False, indent=2)

        return redirect(url_for("profiles"))

    return render_template("form.html")

@app.route("/profiles")
def profiles():
    if not os.path.exists(PROFILE_FILE):
        return "No profiles yet."

    with open(PROFILE_FILE, "r", encoding="utf-8") as f:
        profiles = json.load(f)

    return render_template("profiles.html", profiles=profiles)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10000)
