"""
app/routes.py: Module holds application view functions
"""
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def program():
    user = {'username': 'Macjohnan'}
    posts=[
            {
                'author':{'username':'Steven'},
                'body':'Beatiful day in Uganda'
            },
            {
                'author':{'username':'Efrance'},
                'body':"A mother's happy moments"
            },
            {
                'author':{'username':'Donald Trump'},
                'body':"Enviroment degradation hocks"
            },
            {
                'author':{'username':'Kovosky D'},
                'body':"World cup in Russia"
            }
        ]
    return render_template("index.html", title='Home', user=user, posts=posts)
