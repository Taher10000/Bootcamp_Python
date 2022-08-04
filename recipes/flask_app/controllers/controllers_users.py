from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_app import app
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return redirect('/home')

@app.route("/home")
def home():
    return render_template("home.html")

@app.route('/home/register', methods=["POST"])
def register():
    if not User.validate_registration(request.form):
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    print(request.form)
    data = {
    "first_name": request.form["first_name"],
    "last_name" : request.form["last_name"],
    "email" : request.form["email"],
    "password" : pw_hash
    }
    user_id = User.save(data)
    session['user_id'] = user_id
    print(user_id)
    return redirect('/recipes')

@app.route('/home/login', methods=["POST"])
def login():

    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/recipes')
    

@app.route('/logout')
def logout_user():
    session.clear()
    return redirect('/')


