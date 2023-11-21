from flask import Flask, render_template,jsonify,  redirect, flash,url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db ,Pet
from forms import PetForm,EditPetForm


app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def show_pets():
    pets=Pet.query.all()
    return render_template('pet_list.html',pets=pets)

@app.route('/add/',methods=['GET','POST'])
def add_pet():
    form=PetForm()
    if form.validate_on_submit():
        data={ key: val for key,val in form.data.items() if key != "csrf_token"}
        # pet_name=form.pet_name.data
        # species=form.species.data
        # photo_url=form.photo_url.data
        # age=form.age.data
        # notes=form.notes.data
        # available=form.available.data

        pet = Pet(**data)
        db.session.add(pet)
        db.session.commit()
        flash(f' Added {pet.name} the {pet.species}')
        return redirect(url_for('show_pets'))
    else:
        return render_template('add_pet_form.html',form=form)

@app.route('/<int:pet_id>/',methods=['GET','POST'])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():


        pet.notes=form.notes.data
        pet.available=form.available.data
        pet.photo_url=form.photo_url.data

        db.session.commit()
        flash(f"{pet.name} updated.")

        return redirect(url_for('show_pets'))

    return render_template('edit_pet_form.html',form=form,pet=pet)


@app.route("/api/pets/<int:pet_id>", methods=['GET'])
def api_get_pet(pet_id):
    """Return basic info about pet in JSON."""

    pet = Pet.query.get_or_404(pet_id)
    info = {"name": pet.name, "age": pet.age}

    return jsonify(info)