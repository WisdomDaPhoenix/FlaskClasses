from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import InputRequired,EqualTo



class Newform(FlaskForm):
    msg = "Passwords must match"
    username = StringField('Username',[InputRequired()])
    password = PasswordField('Password',[InputRequired()])
    confirm = PasswordField('Retype Password',[InputRequired(),EqualTo('confirm',message=msg)])
    btnsubmit = SubmitField('Register')








