from flask import Flask, render_template, request
from textdetection import read_image
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

cwd = os.getcwd()

UPLOAD_FOLDER = os.path.join(cwd,'static')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

## To do
## Add a reset link, this will reset all the variable values in the html file.
## Add CSS in the webpage.

@app.route('/', methods=['POST', "GET"])
def image_read():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            # flash('No file part')
            print("File not found!!")
            return render_template('index.html')
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            print("File name empty!")
            # flash('No selected file')
            return render_template('index.html')
        if file and allowed_file(file.filename):
            print("File found", file.filename)
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            detected_text = read_image(file_path, filename)
            print("APP.py ", detected_text)
            saved_file_name = filename.split('.')[0] + "_result.png"
            return render_template('index.html', result = detected_text, user_img = saved_file_name)
        return render_template('index.html')
    return render_template('index.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


if __name__ == "__main__":
    app.run(debug=True)