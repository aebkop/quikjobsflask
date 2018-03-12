from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class addJobs(FlaskForm):
    name = StringField('Name of location')
    jobtype =
    time = StringField()
    days = StringField()
    address = StringField()
    address2 = StringField()
    city = StringField()
    state = StringField()
    postal = StringField()
    web = StringField()
    hours1: StringField()
    hours2: StringField()
    hours3: StringField()


class 3