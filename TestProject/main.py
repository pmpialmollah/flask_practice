from flask import Flask

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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)