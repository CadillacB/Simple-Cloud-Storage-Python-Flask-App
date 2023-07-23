from flask import Flask, render_template, request, redirect, url_for
from google.cloud import storage
import os

app = Flask(__name__,template_folder='templates')

# Set your GCP project ID and bucket name
project_id = "Yourprojectid"
bucket_name = "Yourbucket"
bucket = storage.Client(project=project_id).bucket(bucket_name)


@app.route("/")
def index():
    # List files in the bucket
    blobs = bucket.list_blobs()
    return render_template("index.html", blobs=blobs)


@app.route("/upload", methods=["POST"])
def upload():
    if request.method == "POST" and "file" in request.files:
        file = request.files["file"]
        blob = bucket.blob(file.filename)
        blob.upload_from_file(file)
    return redirect(url_for("index"))

@app.route("/delete/<filename>")
def delete(filename):
    blob = bucket.blob(filename)
    blob.delete()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
