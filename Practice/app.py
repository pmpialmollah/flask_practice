from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql://postgres:1234@localhost:5432/postgres"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Data mode class ------------------------
class User(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    gender = db.Column(db.String)
    department = db.Column(db.String)


# ----------------------------------------


@app.route("/")
def home():
    return "<h1>Home Screen</h1>"


@app.route("/contact")
def contact():
    return "This is contact page!"


@app.route("/users")
def users():
    users = User.query.all()
    result = []

    for data in users:
        result.append(
            {
                "id": data.id,
                "name": data.name,
                "age": data.age,
                "gender": data.gender,
                "department": data.department
            }
        )

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
