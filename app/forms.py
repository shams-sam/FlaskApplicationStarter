from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired

class Form(FlaskForm):
    text = StringField(validators=[DataRequired()])
