from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , BooleanField , SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("username" , validators= [DataRequired()])
    password = StringField("Password" , validators= [DataRequired()])
    remember_me = StringField("Remember me" )
    submit = StringField("Sign in " )