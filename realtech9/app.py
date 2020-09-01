import upload as upload
from flask import Flask, render_template, request
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_dropzone import Dropzone
import os

basedir = os.path.abspath(os.path.dirname(__file__))
upload_dir = os.path.join(basedir, 'uploads')

####################################################
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite" #여기만 바꿔주면 다양한 db와 연동가능
app.config['SECRET_KEY'] = 'sun'
app.config['UPLOADED_PATH'] = upload_dir
# app.config['FLASK_ADMIN_SWATCH'] = 'cerulean' #admin 테마
####################################################

####################################################
db = SQLAlchemy(app) #객체와 db를 연동시킨다. sql처럼 똑같이 사용할 수 있다.
# SQLAlchemy 기능을 갖다쓸 수 있다. 위 아니면 아래 중 하나 쓰면됨. init를 선호.
# db.init_app((app)
admin = Admin(name='test')
admin.init_app(app)
dropzone = Dropzone(app) #
####################################################

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)


admin.add_view(ModelView(User, db.session))
admin.add_view(FileAdmin(upload_dir, name = 'MOON'))

with open("uploads/lec00001_EBS.txt", 'r', encoding='utf-8') as f:
    a = f.read()

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

@app.route("/forward/", methods=['POST'])
def move_forward():
    #Moving forward code
    forward_message = "Moving Forward..."
    return render_template('index.html', forward_message=a);



def pnt(a):
    return a[:30]


# @app.route('/convert')
# def convert():
#     return render_template('RNN.py')

# @app.route('/list')
# def list():
#     for i in User.query.all():
#         print(i)
#         print(i.username)
#         print(i.email)
#     print(User.query.get(1))


if __name__ == '__main__':
    app.run()