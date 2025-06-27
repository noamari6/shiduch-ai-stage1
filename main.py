import os
from flask import Flask, request, render_template
import base64
import json

app = Flask(__name__)

def ask_user(question):
    return input(f"{question}: ")

def analyze_image(image_path):
    return "✔️ התמונה תקינה. אם יש בעיה – נעדכן אותך"

def build_profile():
    profile = {}
    profile['full_name'] = ask_user("מה שמך המלא")
    profile['gender'] = ask_user("מה המין שלך (זכר/נקבה)")
    profile['age'] = ask_user("גיל")
    profile['city'] = ask_user("עיר")
    profile['religious_style'] = ask_user("מה הסגנון הדתי שלך")
    profile['occupation'] = ask_user("במה אתה עוסק")
    profile['looking_for'] = ask_user("מה אתה מחפש בזוגיות")

    image_path = ask_user("העלה את שם הקובץ של תמונתך (בתוך התיקיה)")
    image_feedback = analyze_image(image_path)
    profile['image_feedback'] = image_feedback

    with open(image_path, "rb") as img_file:
        profile['image_base64'] = base64.b64encode(img_file.read()).decode('utf-8')

    with open("profiles.json", "a", encoding="utf-8") as f:
        json.dump(profile, f, ensure_ascii=False)
        f.write(",\n")

    print("✅ כרטיס נוצר!")
    print(json.dumps(profile, indent=2, ensure_ascii=False))

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/profiles")
def show_profiles():
    try:
        with open("profiles.json", "r", encoding="utf-8") as f:
            content = f.read().strip()
            if content.endswith(","):
                content = content[:-1]
            profiles = json.loads(f"[{content}]")
    except:
        profiles = []
    return render_template("profiles.html", profiles=profiles)

if __name__ == "__main__":
    print("שלב יצירת כרטיס – AI בונה עבורך שידוך")
    build_profile()
else:
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
