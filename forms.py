from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SelectField,TextAreaField
from wtforms.validators import Length, Optional,URL,NumberRange


class PetForm(FlaskForm):
    """form for adding pets"""
    name=StringField("Pet Name",)
    species=SelectField("Species",choices=[('cat','Cat'),('dog','Dog'),('porcupine','Porcupine')])

    photo_url=StringField("Photo URL",validators=[URL()])
    age=IntegerField("Age",validators=[NumberRange(min=0,max=30)])
    notes=TextAreaField("Notes")
    available = BooleanField('Available?')

class EditPetForm(FlaskForm):
    photo_url=StringField("Photo URL",validators=[URL(),Optional()])
    notes=TextAreaField("Notes",validators=[Optional(),Length(min=10)])
    available = BooleanField('Available?')




