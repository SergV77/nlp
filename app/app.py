from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h1>Python Flask in Docker!</h1>
    """


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

##python3-pip python3-dev
