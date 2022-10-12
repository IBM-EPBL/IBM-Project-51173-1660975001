from flask import Flask, render_template, url_for
from markupsafe import escape

app=Flask(__name__,template_folder='templates')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/index")
def home():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template("blog.html")    

@app.route('/about')
def about():
    return render_template("Aboutus.html")       

@app.route('/sign-In')
def sign():
    return render_template("Register.html") 
    
     