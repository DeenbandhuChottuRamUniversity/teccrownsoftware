import os
from flask import Flask , request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from flask import Flask , render_template, request
app = Flask(__name__)

# 'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif',
ALLOWED_EXTENSIONS = {'csv'}   # ext. allowed

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
    if file and allowed_file(filename):
        file.save(f"./static/Data CSV/{secure_filename(file.filename)}")
    return redirect('/')

@app.route('/')
def rend():
    return render_template('intern.html');

if __name__ == '__main__':
    app.run(debug=True, port=80)