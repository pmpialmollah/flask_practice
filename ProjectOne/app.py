from flask import Flask, jsonify, request

app = Flask(__name__)

# this index method will execute when user hit the server url
@app.route("/")
def index():
    return "Hello World"

# thid pageNotFound method will execute when user hit any url and it doesn't exist!
@app.errorhandler(404)
def pageNotFound(error):
    return "Web page not found!!!"

# this contactPage method will execute when user hit serverurl/contact
@app.route("/contact")
def contactPage():
    return "This is contact page"


# this aboutPage method will execute when user hit serverurl/about
@app.route("/about")
def aboutPage():
    return "This is about page!"


# this plainText method will execute when user hit serverurl/plaintext
@app.route("/plaintext")
def plainText():
    return "This is plain text."


# this json method will execute when user hit serverurl/json
@app.route("/json")
def json():
    data = {"type": "JSON", "message": "It is a json file."}
    return jsonify(data), 200


# this dynamic method will execute when user hit serverurl/dynamic/<value> and int the value place insert a valid integer
# otherwise it server will raise error
@app.route("/dynamic/<int:value>")
def dynamic(value):
    return f"Your data is: {value}"

# this post method will execute when user request a POST request to server using serverurl/post
@app.route("/post", methods=["POST"])
def post():
    data = request.form.get("post")
    return f"Your post data: {data}"

# this param method will execute when user hit the url with a 'q' parameter like serverurl/param?q=<data> 
@app.route("/param")
def param():
    data = request.args.get("q")
    return f"You asked for: {data}"

# this add method will execute when user hit the url with 'a' and 'b' parameter like serverurl/add?a=<value>&b=<value>
@app.route("/add")
def add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return f"{a} + {b} = {a+b}"

# this form method will execute when user hit serverurl/form with form data respected key 'username' and 'password'
@app.route("/form", methods=["POST"])
def form():
    username = request.form.get("username")
    password = request.form.get("password")
    return f"Login received for {username}"

# user er theke post method er maddhome data niye user registration korar simple code template
@app.route("/registration", methods=["POST"])
def registration():
    username = request.form.get("username", "") 
    email = request.form.get("email", "")
    age = request.form.get("age", "")
    
    if not username or not email or not age:
        return "Missing required fields", 400
    try:
        if int(age) < 13:
            return "Age must be 13 or older", 400
    except ValueError:
        return "Age must me an integer!", 400
    return f"Registration successful for {username}", 200

if __name__ == "__main__":
    app.run(debug=True)
