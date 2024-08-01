from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/pull/<imageName>")
def Docker_image_pull(imageName):
    cmd = f"docker pull {imageName}"
    output = subprocess.getstatusoutput(cmd)

    if output[0] == 0:
        return "Image downloaded successfully."
    else:
        return "Image download failed."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)

