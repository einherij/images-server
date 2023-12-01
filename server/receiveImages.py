import os
from datetime import datetime
from flask import Flask, request


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

@app.route('/')
def defaultListener():
    return "Send images to /send_image/"

@app.route("/send_image/", methods=['GET', 'POST'])
def imageUploader():
    form = """
        <form action="/send_image/" method="POST" enctype="multipart/form-data">
            <input type="file" name="Images" id="images" accept=".jpg, .jpeg, .png" multiple required><hr>
            <input type="submit" value="Send files">
        </form>
    """
    if request.method == "POST":
        for file in request.files.getlist('Images'):
            if in_allowed_files(file.filename):
                path = os.path.join(app.config['UPLOAD_FOLDER'], str(datetime.now())[:10])
                if not os.path.exists(path):
                    os.makedirs(path)
                file.save(os.path.join(path, file.filename))

    return form

def in_allowed_files(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app.run(host="0.0.0.0", port=8900, debug=False)