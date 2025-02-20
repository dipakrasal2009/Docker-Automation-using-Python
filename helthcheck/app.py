from flask import Flask
import sys
import time

time.sleep(50)

app = Flask(__name__)
data=sys.argv[1]

@app.route("/")
def HC():
    return "hello from Dipak..........."

app.run(host="0.0.0.0")
