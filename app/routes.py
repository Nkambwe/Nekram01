"""
app/routes.py: uses the render_template() function
"""
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Macjohnan'}
    return render_template("index.html", user=user)
