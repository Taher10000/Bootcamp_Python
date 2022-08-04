from flask import render_template,redirect,request,session,flash
from flask_app.models.recipe import Recipe
from flask_app import app
from flask import flash
from flask_bcrypt import Bcrypt
import requests
import os
from flask import jsonify

bcrypt = Bcrypt(app)


@app.route("/recipes")
def recipes():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'user_id': session['user_id'],
        'id': session['user_id']
    }
    print(recipes)
    list_recipes = Recipe.get_all_with_recipe()
    return render_template("recipes.html", list_recipes = list_recipes)

@app.route('/recipes/<int:id>')
def show_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    recipe_data = {
        'id': id
    }
    user_data = {
        'id': session['user_id']
    }
    return render_template('recipe_show_id.html', recipe=Recipe.get_from_id(recipe_data))

@app.route('/recipes/new')
def new():
    return render_template("new.html")


@app.route('/recipes/create', methods=["POST"])
def create():
    if 'user_id' not in session:
        return redirect('/')
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    data = {
    "name": request.form["name"],
    "description" : request.form["description"],
    "thirty_min" : request.form["thirty_min"],
    "instructions" : request.form["instructions"],
    "date_cooked" : request.form["date_cooked"],
    "user_id" : session["user_id"]
    }
    Recipe.save(data)
    return redirect("/recipes")




@app.route('/recipes/edit/<int:id>')
def edit(id):
    recipe_data = {
        "id": id
    }
    user_data = {
        'id': session['user_id']
    }
    return render_template('recipes_edit.html', recipe=Recipe.get_from_id(recipe_data))



@app.route('/recipes/update/<int:id>', methods=["POST"])
def update(id):
    if 'user_id' not in session:
        return redirect('/')
    if not Recipe.validate_recipe(request.form):
        return redirect(f'/recipes/edit/{id}')
    data = {
        'id': id,
        'name': request.form['name'],
        'instructions': request.form['instructions'],
        'date_cooked': request.form['date_cooked'],
        'description': request.form['description'],
        'user_id': session['user_id']
        }
    Recipe.update(data)
    return redirect('/recipes')

@app.route('/api/recipes/all', methods=["POST"])
def api_recipes():
    print(f"https://api.spoonacular.com/food/products/search?query={request.form['query']}&apiKey={os.environ.get('FLASK_APP_API_KEY')}")
    r = requests.get(f"https://api.spoonacular.com/food/products/search?query={request.form['query']}&apiKey={os.environ.get('FLASK_APP_API_KEY')}")
    return jsonify( r.json() )

@app.route('/recipes/all')
def all_recipes_show():
    return render_template("all.html")

@app.route('/recipes/delete/<int:id>')
def recipes_destroy(id):
    data = {
        "id": id
    }
    Recipe.delete(data)
    return redirect('/recipes')



