import upload as upload
import os
from flask import Flask, render_template, request
from flask_dropzone import Dropzone
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__) #1. 연결시킨다
basedir = os.path.abspath(os.path.dirname(__file__))
upload_dir = os.path.join(basedir, 'uploads')

#####################################################
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite" #여기만 바꿔주면 다양한 db와 연동가능
app.config['SECRET_KEY'] = 'sun'
app.config['UPLOADED_PATH'] = upload_dir
#####################################################

# DB #################################################
db = SQLAlchemy(app) #객체와 db를 연동시킨다. sql처럼 똑같이 사용할 수 있다.

class User(db.Model):  #db.Model을 상속받음
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)

# SQLAlchemy 기능을 갖다쓸 수 있다. 위 아니면 아래 중 하나 쓰면됨. init를 선호.
# db.init_app((app)
admin = Admin(name='test')
admin.init_app(app)
admin.add_view(ModelView(User, db.session)) #정말 별거없다
admin.add_view(FileAdmin(upload_dir, name='MOON'))
####################################################


# Drop zone #################################################
dropzone = Dropzone(app) #
####################################################


@app.route('/')
def main():
    return render_template('home.html')

@app.route('/math')
def mathlist():
    return render_template('list1.html')

@app.route('/a')
def list():
    return render_template('index2.html')

@app.route('/s', methods=['GET', 'POST'])
def upload():
    if request.method =='POST':
        f = request.files.get('file')
        f.save(os.path.join(upload_dir, f.filename))
    return render_template('stt.html')

@app.route('/d')
def dand():
    return render_template('dd.html')


if __name__ == '__main__':
    app.run()
