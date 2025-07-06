from flask import Flask

app = Flask(__name__)

@app.route("/info")
def lwinfo():
        return "I am Lw from India"

@app.route("/phone")
def lwphone():
        return "8003622847"

app.run(host="0.0.0.0")