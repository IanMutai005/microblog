from flask import render_template
from app import app 

@app.route("/")
@app.route("/index")
def index():

    user = {'username' : 'Martin'}
    posts = [
        {
            'author' : {'username':'Ian'},
            'body' : 'Beautiful day in Nairobi'
        },
        {
            'author' : {'username':'Mutai'},
            'body' : 'Arsenal is the greatest team ever'
        }
    ]
    return render_template('index.html',title = 'Home', user = user , posts =posts)