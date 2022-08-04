from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    users = User.get_all()
    print(users)
    return redirect('/home')

@app.route("/home")
def home():
    return render_template("home.html", users = User.get_all())

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
    return redirect('/dashboard')

@app.route('/home/login', methods=["POST"])
def login():

    # see if the username provided exists in the database
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    # never render on a post!!!
    return redirect('/dashboard')

@app.route("/dashboard")
def new():
    user = User.get_one({'id':session['user_id']})
    return render_template("dashboard.html", user = user)



# @app.route('/users/show/<int:id>')
# def show(id):
#     data = {
#         "id": id
#     }
#     return render_template('show.html', user = User.get_one(data))

# @app.route('/users/edit/<int:id>')
# def edit(id):
#     data = {
#         "id": id
#     }
#     return render_template('edit.html', user = User.get_one(data))

# @app.route('/users/update', methods=["POST"])
# def update():
#     User.update(request.form)
#     return redirect('/users')

# @app.route('/users/destroy/<int:id>')
# def destroy(id):
#     data = {
#         "id": id
#     }
#     User.destroy(data)
#     return redirect('/users')



