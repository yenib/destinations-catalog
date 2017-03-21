from itemCatalog import app, db
from itemCatalog.forms import CategoryForm
from itemCatalog.models import Category

from flask import flash, render_template, request, redirect, url_for
from werkzeug.exceptions import HTTPException, abort


@app.route('/')
@app.route('/destinations')
def home():
    return "List of destinations goes here."



@app.route('/destination/new/')
def newItem():
    return "New Destination goes here."


@app.route('/destination/<int:item_id>/')
def showItem(item_id):
    return "Show Destination goes here."


@app.route('/destination/<int:item_id>/edit')
def editItem(item_id):
    return "Edit Destination goes here."


@app.route('/destination/<int:item_id>/delete')
def deleteItem(item_id):
    return "Delete Destination goes here."





@app.route('/categories')
def listCategories():
    cats = Category.query.all()
    return render_template('categories.html', categories=cats)


@app.route('/category/new/', methods=['GET', 'POST'])
def newCategory():
    form = CategoryForm(request.form)
    if form.validate_on_submit():
        cat = Category(form.name.data, form.description.data)
        db.session.add(cat)
        db.session.commit()
        flash('The category was successfully created.', "success")
        return redirect(url_for('listCategories'))
    return render_template('newCategory.html', form=form)


@app.route('/category/<int:category_id>/edit', methods=['GET', 'POST'])
def editCategory(category_id):
    cat = Category.query.get_or_404(category_id)
    form = CategoryForm(request.form, obj=cat)
    form.name.default = cat.name
    if form.validate_on_submit():
        cat.name = form.name.data
        cat.description = form.description.data
        db.session.add(cat)
        db.session.commit()
        flash('The category was successfully updated.', "success")
        return redirect(url_for('listCategories'))
    return render_template('editCategory.html', form=form, category=cat)


@app.route('/category/<int:category_id>/delete', methods=['POST'])
def deleteCategory(category_id):
    cat = Category.query.get_or_404(category_id)
    if cat.items.all():
        flash(('The category cannot be deleted because there are '
               'Destinations that point to it.'), "danger")
    else:
        db.session.delete(cat)
        db.session.commit()
        flash('The category was successfully deleted.', "success")
    return redirect(url_for('listCategories'))






