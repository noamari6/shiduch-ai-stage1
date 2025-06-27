from flask import Flask, request, render_template

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

    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
