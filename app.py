from flask import Flask, render_template

app = Flask(__name__)

subjects = ['Python','Database','Data Science','Java']

@app.route("/")
def index():
    return render_template('index.html',name='Jack', subjects=subjects)

@app.route("/about")
def about():
    return 'I am zoti. Welcome to my class.'