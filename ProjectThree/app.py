from flask import Flask, request, render_template, redirect

app = Flask(__name__)

# --------------------------------------------------------
# user class
class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def getName(self):
        return self.name

    def getEmail(self):
        return self.email

    def getAge(self):
        return self.age
# --------------------------------------------------------

# --------------------------------------------------------
# users list
users = []
# --------------------------------------------------------


@app.route("/")
def index():
    return "Welcome to Flask WebApp"


@app.errorhandler(404)
def pageNotFound(err):
    return "No page found, dude!"



@app.route("/adduser", methods=["POST"])
def addUser():
    userName = request.form.get("name")
    userEmail = request.form.get("email")
    userAge = request.form.get("age")

    if not userName or not userEmail or not userAge:
        return "All information required!"
    try:
        ageInt = int(userAge)
        if ageInt<15:
            return "Age must be 15 or older!"
    except ValueError:
        return "Age must be in integer!"
    
    userId = len(users) + 1
    user = User(userName, userEmail, ageInt)
    item = {
        "id" : userId,
        "user" : user
    }
    users.append(item)
    return redirect("/userlist")

@app.route("/userlist")
def userList():
    return render_template("index.html", data = users, len = len(users))


if __name__ == "__main__":
    app.run(debug=True)
