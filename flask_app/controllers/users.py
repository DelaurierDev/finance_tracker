from flask_app import app
from flask import render_template, redirect,request,session,flash
import re
from flask_app.models.user import User
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#Render the landing page
@app.route('/')
def landing():
    return render_template('/index.html')

@app.route('/signin')
def login_reg():
    return render_template('/signin.html')