import os

from itemCatalog import app, db
from itemCatalog.forms import CategoryForm, ItemForm, LoginForm
from itemCatalog.models import Category, Item, User

from flask import (flash, render_template, request,
                   redirect, url_for, send_from_directory)

from  flask_login.utils import login_required, login_user, logout_user


from werkzeug.utils import secure_filename
from werkzeug.datastructures import CombinedMultiDict, FileStorage

from sqlalchemy.orm import defer
from sqlalchemy.sql.expression import and_


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


def removeFile(filename):
    file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.isfile(file):
        os.remove(file)

        

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
                    categoryId=form.category.data,
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
    item = Item.query.get_or_404(item_id)
    relatedItems = Item.query.options(defer("description")).filter(
                        and_(Item.country.ilike(item.country),
                             Item.id != item.id)).order_by(
                                Item.id.desc()).limit(3).all()
    return render_template('showItem.html', item=item,
                           relatedItems=relatedItems)



@app.route('/destination/<int:item_id>/edit', methods=['GET', 'POST'])
def editItem(item_id):
    item = Item.query.get_or_404(item_id)
    form = ItemForm(CombinedMultiDict((request.files, request.form)), obj=item)
    form.category.choices = getChoicesOfCategorySelect()
    form.image.default = item.image
    if request.method == 'GET':
        form.category.default = item.categoryId
        form.category.process([])
    elif form.validate():
        if isinstance(form.image.data, FileStorage) and form.image.data:
            filename = secure_filename(form.image.data.filename)
            removeFile(item.image)
            saveFile(form.image.data, filename)
            item.image = filename
        
        item.name = form.name.data
        item.categoryId = form.category.data
        item.coutry = form.country.data
        item.description = form.description.data
        item.location = form.location.data
        item.imageAlt = form.imageAlt.data
        db.session.add(item)
        db.session.commit()
        flash('The destination was successfully updated.', "success")
        return redirect(url_for('showItem', item_id=item.id))
    return render_template('editItem.html', form=form, item=item)



@app.route('/destination/<int:item_id>/delete', methods=['POST'])
def deleteItem(item_id):
    item = Item.query.get_or_404(item_id)
    removeFile(item.image)
    db.session.delete(item)
    db.session.commit()
    flash('The destination was successfully deleted.', "success")
    return redirect(url_for('home'))
    


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



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).one()
        login_user(user)

        flash('Logged in successfully.', 'success')

        return redirect(url_for('home'))
    return render_template('login.html', form=form)



@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "success")
    return redirect(url_for('home'))
