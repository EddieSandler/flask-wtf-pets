from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import Email, Optional,URL,AnyOf,NumberRange


class NewPetForm(FlaskForm):
    """form for adding pets"""
    pet_name=StringField("Pet Name",)
    species=StringField("Species",validators=[AnyOf(values=['cat','dog','porcupine'])])

    photo_url=StringField("Photo URL",validators=[URL(require_tld=False,message=None)])
    age=IntegerField("Age",validators=[NumberRange(min=0,max=30)])
    notes=StringField("Notes")
    available = BooleanField('Available')


class EditPetForm(FlaskForm):
    notes = StringField('Notes')
    available = BooleanField('Available')
    photo_url=StringField("Photo URL",validators=[URL(require_tld=False,message=None)])