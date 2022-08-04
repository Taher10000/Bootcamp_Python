from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/")
def index():
    dojos = Dojo.get_all()
    print(users)
    return redirect('/dojos')

@app.route("/dojos")
def users():
    return render_template("dojos.html", dojos = Dojo.get_all())

@app.route("/dojos/show/<int:dojo_id>")
def dojo_detail(dojo_id):
    data = {'id': dojo_id}
    dojo_data = Dojo.get_dojo_with_ninjas(data)
    print(dojo_data.ninjas)
    return render_template('dojo_show.html', dojo_data=dojo_data)

# @app.route('/dojos/show/<int:id>')
# def show(id):
#     data = {
#         "id": id
#     }
#     return render_template('dojo_show.html', ninjas = Ninja.get_all())

@app.route("/dojos/new")
def new():
    return render_template("new_ninjas.html", dojos = Dojo.get_all())

@app.route('/dojos/create', methods=["POST"])
def create():
    dojo_id = Ninja.save(request.form)
    return redirect(f"/dojos/show/{request.form['dojo_id']}")

@app.route('/dojos/new_dojo', methods=["POST"])
def new_dojo():
    print(request.form)
    data = {
    "name": request.form["name"]
    }
    Dojo.save(data)
    return redirect('/dojos')

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



