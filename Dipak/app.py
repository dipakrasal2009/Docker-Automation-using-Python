
from flask import Flask

app = Flask(__name__)

@app.route("/")
def myfunc():
    return "Hello From Dipak........."

app.run(host="0.0.0.0")
