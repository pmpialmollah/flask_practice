from flask import Flask, request

app = Flask(__name__)

@app.errorhandler(404)
def pageNotFound(e):
    return "Not page found brother."

@app.route("/")
def index():
    return  "Flask server is running..."

@app.route("/about")
def about():
    return "This is about page."

@app.route("/args")
def getDataFromArguments():
    name = request.args.get("name")
    return f"Your name is {name}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)