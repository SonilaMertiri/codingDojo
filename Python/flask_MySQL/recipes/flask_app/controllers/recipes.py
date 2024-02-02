from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.recipe import Recipe
from flask_app.models.user import User


@app.route('/recipes/new')
def addRecipe():
    if 'user_id' in session:
        return render_template('addRecipe.html')
    return redirect('/')


@app.route('/recipes/new', methods=['POST'])
def create_recipe():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'under_30': request.form.get('under_30', ''),
        'user_id':session['user_id']
    }

    is_valid=Recipe.validate_recipe_content(data)
    if  is_valid:
        Recipe.save(data)
        return redirect('/')
    return redirect(request.referrer)

@app.route('/recipes/show/<int:id>')
def show_recipes(id):
    if 'user_id' not in session:
        return redirect('/')
    data={
        'id':id
    }
    recipe= Recipe.get_recipe_by_id(data)
    if recipe:
        return render_template('viewRecipe.html', recipe=recipe)
    return redirect('/')


@app.route('/recipes/edit/<int:id>')
def edit_recipes(id):
    if 'user_id' not in session:
        return redirect('/')
    data={
        'id':id
    }
    recipe= Recipe.get_recipe_by_id(data)
    if recipe and recipe['user_id']== session['user_id']:
        return render_template('editRecipe.html', recipe=recipe)
    return redirect('/')


@app.route('/recipes/edit/<int:id>', methods=['POST'])
def update_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    data={
        'id':id
    }
    recipe= Recipe.get_recipe_by_id(data)
    if recipe and recipe['user_id']== session['user_id']:
        data = {
            'name': request.form.get('name'),
            'description': request.form.get('description'),
            'instructions': request.form.get('instructions'),
            'under_30': request.form.get('under_30', ''),
            'id': id
        }
        is_valid= Recipe.validate_recipe_content(data)
        if is_valid:
            Recipe.update(data)
            return redirect('/')
        # return redirect('/recipes/' + str(id))
    return redirect(request.referrer)


@app.route('/recipes/delete/<int:id>')
def delete_recipes(id):
    if 'user_id' not in session:
        return redirect('/')
    data={
        'id': id
    }
    recipe= Recipe.get_recipe_by_id(data)
    if recipe['user_id']== session['user_id']:
        Recipe.deleteRecipe(data)
    return redirect('/')
