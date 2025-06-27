from flask import Flask, request, render_template_string

app = Flask(__name__)

form_html = """
<!DOCTYPE html>
<html>
<head>
    <title>שידוך AI – יצירת כרטיס</title>
</head>
<body>
    <h2>יצירת כרטיס – שלב א'</h2>
    <form method="post">
        <label>מה שמך המלא?</label><br>
        <input type="text" name="full_name" required><br><br>

        <label>בן/בת כמה אתה/את?</label><br>
        <input type="number" name="age" required><br><br>

        <button type="submit">שלח</button>
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        full_name = request.form.get("full_name")
        age = request.form.get
