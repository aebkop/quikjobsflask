from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField, Form
from wtforms import validators

class addJobs(FlaskForm):
    name = StringField('Name of location')
    jobtype = RadioField("Jobtype", choices=[('Waiter','Waiter'),('Chef','Chef'),('Office','Offices'),('Other','Other ')])
    time = RadioField("Times", choices=[('Morning','Morning'),('Evening','Evening'),('Night','Night')])
    days = RadioField("Days",choices=[('Weekdays','Weekdays'),('Weekends','Weekends')])
    address = StringField("Address")
    address2 = StringField("Adress2")
    city = StringField("City")
    state = StringField("County")
    postal = StringField("Postal")
    web = StringField("Web")
    hours1: StringField("Hours")
    hours2: StringField()
    hours3: StringField()