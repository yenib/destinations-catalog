import os

from itemCatalog import app, db
from itemCatalog.forms import CategoryForm, ItemForm
from itemCatalog.models import Category, Item

from flask import (flash, render_template, request,
                   redirect, url_for, send_from_directory)

from werkzeug.utils import secure_filename
from werkzeug.datastructures import CombinedMultiDict

from sqlalchemy.orm import defer


def getChoicesOfCategorySelect():
    choices = [(0, 'Select a category')]
    cats = Category.query.options(defer("description")).all()
    choices.extend([(c.id, c.name) for c in cats])
    return choices



def saveFile(file, filename):
    if file:
        if not filename:
            filename = secure_filename(file.filename)
        #TODO: resolve name's conflicts    
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))



@app.route('/picture/<path:filename>')
def downloadFile(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)



@app.route('/')
@app.route('/destinations')
def home():
    items = Item.query.options(defer("description")).order_by(
        Item.id.desc()).all()
    return render_template("items.html", items=items)



@app.route('/destination/new/', methods=['GET', 'POST'])
def newItem():
    form = ItemForm(CombinedMultiDict((request.files, request.form)))    
    form.category.choices = getChoicesOfCategorySelect()
    if form.validate_on_submit():
        filename = secure_filename(form.image.data.filename)
        saveFile(form.image.data, filename)
        item = Item(name=form.name.data,
                    category=form.category.data,
                    country=form.country.data,
                    description=form.description.data,
                    location=form.location.data,
                    image=filename,
                    imageAlt = form.imageAlt.data)
        db.session.add(item)
        db.session.commit()
        flash('The destination was successfully created.', "success")
        return redirect(url_for('home'))
    return render_template('newItem.html', form=form)



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
    if cat.items.first():
        flash(('The category cannot be deleted because there are '
               'Destinations that point to it.'), "danger")
    else:
        db.session.delete(cat)
        db.session.commit()
        flash('The category was successfully deleted.', "success")
    return redirect(url_for('listCategories'))






