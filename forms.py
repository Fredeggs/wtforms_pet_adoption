import requests
from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, Optional, URL, ValidationError
from wtforms import (
    StringField,
    FloatField,
    BooleanField,
    IntegerField,
    RadioField,
    SelectField,
)

species_list = ["cat", "dog", "porcupine"]


def check_age(form, field):
    if field.data < 0 or field.data > 30:
        raise ValidationError("Age must be between 0 and 30")


def check_url(form, field):
    response = requests.get(field.data)
    if response.status_code != 200:
        raise ValidationError('Please Enter A Valid URL')


class PetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators=[
        InputRequired(message="Snack field can't be blank")])
    species = SelectField(
        "Species", choices=[(species, species) for species in species_list])
    photo = StringField("Photo of Pet", validators=[
        check_url,
        URL(),
        Optional()])
    age = IntegerField("Age of Pet", validators=[check_age])

    notes = StringField("Description/Notes about the Pet")

    availability = RadioField(
        "Available?",
        choices=[
            (True, "Available"),
            (False, "Unavailable"),
        ],)
