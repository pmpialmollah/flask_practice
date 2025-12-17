from flask import Flask, render_template, request
import time

app = Flask(__name__)

# -------------------------------------------
users = []
# -------------------------------------------


@app.route("/")
def index():
    return render_template("index.html")


@app.errorhandler(404)
def pageNotFound(err):
    return "Page not found, dude!"


@app.route("/adduser", methods=["POST"])
def addUser():
    username = request.form.get("username")
    if not username:
        return "All information required!"
    if username in users:
        return "Name is already existed! try another."

    users.append(username)
    data = "User added successfully."
    return render_template("adduser.html", response=data), 200

@app.route("/userlist")
def userList():
    return render_template("userlist.html", data = users), 200
    



if __name__ == "__main__":
    app.run(debug=True)
