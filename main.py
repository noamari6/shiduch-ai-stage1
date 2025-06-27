from flask import Flask, request, render_template_string
import json
import os

app = Flask(__name__)

def ask_user(question):
    return input(f"{question}: ")

def build_profile():
    profile = {}
    profile['full_name'] = ask_user("מה שמך המלא")
    profile['age'] = ask_user("בן/בת כמה אתה/את")
    profile['city'] = ask_user("מה העיר שבה אתה גר")
    profile['religious_level'] = ask_user("מה רמת הדתיות שלך")
    profile['about'] = ask_user("כתוב בקצרה משהו על עצמך")
    return profile

@app.route("/", methods=["GET"])
def form():
    return render_template_string(open("form.html", encoding="utf-8").read())

@app.route("/submit", methods=["POST"])
def submit():
    profile = {
        "full_name": request.form["full_name"],
        "age": request.form["age"],
        "city": request.form["city"],
        "religious_level": request.form["religious_level"],
        "about": request.form["about"]
    }

    # שמירת הפרופיל לקובץ
    if not os.path.exists("profiles.json"):
        profiles = []
    else:
        with open("profiles.json", "r", encoding="utf-8") as f:
            profiles = json.load(f)

    profiles.append(profile)

    with open("profiles.json", "w", encoding="utf-8") as f:
        json.dump(profiles, f, indent=2, ensure_ascii=False)

    return f"תודה {profile['full_name']}! הפרופיל שלך התקבל."

@app.route("/profiles", methods=["GET"])
def show_profiles():
    if not os.path.exists("profiles.json"):
        return "לא קיימים כרטיסים במערכת עדיין."

    with open("profiles.json", "r", encoding="utf-8") as f:
        profiles = json.load(f)

    html = "<h1>כרטיסים קיימים:</h1>"
    for p in profiles:
        html += f"<div><b>{p['full_name']}</b>, {p['age']}, {p['city']}<br>{p['religious_level']}<br>{p['about']}<hr></div>"

    return html

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
