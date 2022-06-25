from crypt import methods
from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from forms import PetForm
from models import (
    Pet,
    db,
    connect_db,
)

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pets_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "chickenz123"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
deb = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def list_pets():
    pets = Pet.query.all()
    return render_template("index.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    form = PetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo = form.photo.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species,
                      photo_url=photo, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("add-pet.html", form=form)

@app.route("/<pet_id>")
def show_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    return render_template("pet-details.html", pet=pet)

@app.route("/<pet_id>/edit", methods=["GET","POST"])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = PetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.photo_url = form.photo.data
        pet.available = form.availability.data
        db.session.commit()
        return redirect('/')
    else:
        return render_template('edit-pet.html', form=form, pet=pet)