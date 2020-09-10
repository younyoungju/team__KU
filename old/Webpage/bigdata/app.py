from flask import Flask, render_template, request

# from flask_sqlalchemy import SQLAlchemy
# from flask_admin.contrib.sqla import ModelView
# from flask_admin import Admin
# import upload as upload
# from flask_admin.contrib.fileadmin import FileAdmin
import os
import sqlite3

basedir = os.path.abspath(os.path.dirname(__file__))
upload_dir = os.path.join(basedir, 'uploads')




@app.route('/')
def main():
    return render_template('home.html')



#
#
# @app.route('/s', methods=['GET', 'POST'])
# def upload():
#     if request.method == 'POST':
#         f = request.files.get('file')
#         f.save(os.path.join(upload_dir, f.filename))
#
#     return render_template('stt.html')


@app.route('/l')
def lectures():
    conn = sqlite3.connect('db')
    c = conn.cursor()
    for row in c.execute('SELECT * FROM '):
        data = row
    conn.close()
    return render_template('Lectures.html',data=data)


# @app.route('/data')
# def data():
#     for i in User.query.all():
#         print(i)
#         print(i.username)
#         print(i.email)
#         print(User.query.get(1))
    # basedir = os.path.abspath(os.path.dirname(__file__))
    # print(basedir)


if __name__ == '__main__':
    app.run()
