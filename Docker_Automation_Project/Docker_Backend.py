def Docker_image_pull(imageName):
    cmd = f"docker pull {imageName}"
    output = subprocess.getstatusoutput(cmd)

    if output[0] == 0:
        return "Image downloaded successfully."
    else:
        return "Image download failed."

@app.route("/run/<imageName>")
def Docker_image_run(imageName):
    cmd = f"docker run -dit {imageName}"
    output = subprocess.getstatusoutput(cmd)

    if output[0] == 0:
        return "image Run Successfully..."
    else:
        return "image run failed..."

@app.route("/stop/<imageName>")
def Docker_image_stop(imageName):
    cmd = f"docker stop {imageName}"
    output = subprocess.getstatusoutput(cmd)

    if output[0] == 0:
        return "Image stopped successfully..."
    else:
        return "Image stopped Failed..."


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=83)
