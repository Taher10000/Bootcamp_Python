from crypt import methods
from flask import render_template, request, redirect
# import the class from friend.py
from models.user import User

from flask_app import app
# ...server.py





@app.route("/")
def index():
    # call the get all classmethod to get all friends 
    users = User.get_all()
    print(users)
    return redirect('/users')

@app.route("/users")
def users():
    # call the get all classmethod to get all friends 
    return render_template("read.html", users = User.get_all())

# relevant code snippet from server.py

@app.route("/users/new")
def new():
    # call the get all classmethod to get all friends 
    users = User.get_all()
    print(users)
    return render_template("create.html", users = users)

@app.route('/users/create', methods=["POST"])
def create():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    print(request.form)
    data = {
    "first_name": request.form["first_name"],
    "last_name" : request.form["last_name"],
    "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/users')

@app.route('/users/edit/<int:id>')
def edit(id):
    data = {
        "id": id
    }
    return render_template('edit.html', user = User.get_one(data))

@app.route('/users/update', methods=["POST"])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/users/destroy/<int:id>')
def destroy(id):
    data = {
        "id": id
    }
    User.destroy(data)
    return redirect('/users')

@app.route('/users/show/<int:id>')
def show(id):
    data = {
        "id": id
    }
    return render_template('show.html', user = User.get_one(data))

if __name__ == "__main__":
    app.run(debug=True)

