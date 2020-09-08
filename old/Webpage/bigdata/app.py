from flask import Flask, render_template, request
from flask_dropzone import Dropzone
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
import upload as upload
from flask_admin.contrib.fileadmin import FileAdmin
import os

basedir = os.path.abspath(os.path.dirname(__file__))
upload_dir = os.path.join(basedir, 'uploads')

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
app.config['SECRET_KEY'] = 'bana'
app.config['UPLOADED_PATH'] = upload_dir
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
admin = Admin(app, name='Test')

Dropzone(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)


admin.add_view(ModelView(User, db.session))
admin.add_view(FileAdmin(upload_dir, name='Files'))


@app.route('/')
def main():
    return render_template('home.html')


@app.route('/math')
def mathlist():
    return render_template('list1.html')


@app.route('/a')
def index2():
    return render_template('index2.html')


@app.route('/s', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join(upload_dir, f.filename))

    return render_template('stt.html')


@app.route('/convert/')
def convert():
    return render_template('RNN.py')


@app.route('/data')
def data():
    for i in User.query.all():
        print(i)
        print(i.username)
        print(i.email)
        print(User.query.get(1))
    # basedir = os.path.abspath(os.path.dirname(__file__))
    # print(basedir)


if __name__ == '__main__':
    app.run()
