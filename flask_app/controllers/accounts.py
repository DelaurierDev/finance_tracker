from flask_app import app
from flask import render_template, redirect,request,session,flash

@app.route("/dashboard")
def dash():
    return render_template("/dashboard.html")