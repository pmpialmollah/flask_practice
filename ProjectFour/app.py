from flask import Flask, render_template, request, jsonify

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

@app.route("/plain")
def plainText():
    return render_template("adduser.html", response="Server Response")

@app.route("/json")
def json():
    data = [1, 2, 3, 4]
    return jsonify(data), 200


@app.route("/userlist")
def userList():
    return render_template("userlist.html", data=users), 200


@app.route("/addbyparam")
def addByParam():
    username = request.args.get("username")
    if not username:
        return "Please enter user name through params."
    if username in users:
        return "Name already existed! try another..."

    users.append(username)
    data = "User added successfully."
    return render_template("adduser.html", response=data), 200


if __name__ == "__main__":
    app.run(debug=True)
