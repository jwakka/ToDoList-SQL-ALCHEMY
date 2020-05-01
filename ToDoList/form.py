from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, validators
from wtforms.validators import Length, DataRequired

class ToDoList(FlaskForm):
    message = TextAreaField("ToDo",  [validators.Required("Please enter a message.")])
    submit = SubmitField("Submit")


