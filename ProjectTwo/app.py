from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():

    list = {"bangla", "english", "math", "physics"}
    return render_template("index.html", name="PIAL", list=list)


@app.route("/students")
def students():
    students = [
        {"name": "Rafi", "marks": 85},
        {"name": "Sumi", "marks": 92},
        {"name": "Tariq", "marks": 74},
    ]
    return render_template("profile.html", data = students)


if __name__ == "__main__":
    app.run(debug=True)
