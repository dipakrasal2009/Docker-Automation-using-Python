from flask import Flask

app = Flask(__name__)

@app.route("/")
def HC():
    return "hello from Dipak..........."

app.run(host="0.0.0.0")
