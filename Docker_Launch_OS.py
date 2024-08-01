import subprocess 

from flask import Flask

app = Flask (__name__)

@app.route("/   Dipak")
def Docker_Launch():
    cmd = f"cal"

    cid = subprocess.getoutput(cmd)

    return f"Docker Launch Successfully...  : {cal}"



app.run(port = 80,host = "0.0.0.0")
