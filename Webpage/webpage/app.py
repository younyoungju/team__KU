from flask import Flask, render_template
import os
import sqlite3
from flask_paginate import Pagination
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
upload_dir = os.path.join(basedir, '../../Documents/team__KU1/Webpage/bigdata/uploads')


@app.route('/')
def main():
    return render_template('home.html')


@app.route('/math')
def mathlist():
    return render_template('list1.html')

@app.route('/Lecture')
@app.route('/Lecture/<int:page>')
def index2(page=1):
    per_page = 5
    offset = per_page
    conn = sqlite3.connect('LectList.db')
    cur = conn.cursor()
    data = cur.execute("SELECT count(*) FROM Lec_list").fetchone()
    lecs = cur.execute("SELECT * FROM Lec_list ORDER BY lec_id ASC LIMIT ?,?",(per_page*(page-1), offset)).fetchall()
    pagination = Pagination(page=page, per_page=per_page, offset=offset, total=data[0], record_name='Lec_list', css_framework='foundation')
    conn.close()
    return render_template('Lectures.html', data=lecs, pagination=pagination)

@app.route('/video/<id>')
def videos(id):
    conn = sqlite3.connect('LectList.db')
    cur = conn.cursor()
    data = cur.execute("SELECT * FROM Lec_list WHERE lec_id=?",[id,]).fetchone()
    return render_template('Video.html', data=data)



if __name__ == '__main__':
    app.run()
