from flask import Flask, render_template,  redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db ,Pet
from forms import NewPetForm,EditPetForm


app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def show_pets():
    pets=Pet.query.all()
    return render_template('pet_list.html',pets=pets)

@app.route('/add',methods=['GET','POST'])
def add_pet_form():
    form=NewPetForm()
    if form.validate_on_submit():
        pet_name=form.pet_name.data
        species=form.species.data
        photo_url=form.photo_url.data
        age=form.age.data
        notes=form.notes.data
        available=form.available.data

        pet = Pet(name=pet_name, species=species, photo_url=photo_url,age=age,notes=notes,available=available)
        db.session.add(pet)
        db.session.commit()
        flash(f' Added {pet.name} the {species}')
        return redirect('/add')
    else:
        return render_template('add_pet_form.html',form=form)

@app.route('/<int:pet_id>',methods=['GET','POST'])
def display_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        form.populate_obj(pet)
        db.session.commit()
        flash(f' Edited  {pet.name}')
        return redirect('/<pet_id>')

    return render_template('edit_pet_form.html',form=form,pet=pet)