from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Email, Optional


class NewPetForm(FlaskForm):
    """form for adding pets"""
    pet_name=StringField("Pet Name")
    species=StringField("Species")
    photo_url=StringField("Photo URL")
    age=IntegerField("Age")
    notes=StringField("Notes")