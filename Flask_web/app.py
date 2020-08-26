from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Welcome to Tech-9!'

@app.route('/math')
def mathlist():
    return render_template('list1.html')

@app.route('/a')
def list():
    return render_template('index2.html')


if __name__ == '__main__':
    app.run()