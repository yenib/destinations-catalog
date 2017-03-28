import os

from itemCatalog import app, db
from itemCatalog.forms import CategoryForm, ItemForm, LoginForm
from itemCatalog.models import Category, Item, User
from itemCatalog.extensions import admin_permission

from flask import (flash, render_template, request, abort,
                   redirect, url_for, send_from_directory, current_app)

from flask_login.utils import (login_required, login_user,
                               logout_user, current_user)
from flask_principal import (identity_changed, AnonymousIdentity, Identity,
                             Permission, UserNeed)


from werkzeug.utils import secure_filename
from werkzeug.datastructures import CombinedMultiDict, FileStorage

from sqlalchemy.orm import defer
from sqlalchemy.sql.expression import and_, or_


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

        

@app.route('/picture/<path:filename>/')
def downloadFile(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)



@app.route('/')
@app.route('/destinations/')
def home():
    items = Item.query.options(defer("description")).order_by(
        Item.id.desc()).all()
    categories = Category.query.all()
    return render_template("items.html", items=items, categories=categories)



@app.route('/destination/new/', methods=['GET', 'POST'])
#@login_required
def newItem():
    form = ItemForm(CombinedMultiDict((request.files, request.form)))    
    form.category.choices = getChoicesOfCategorySelect()
    if form.validate_on_submit():
        filename = secure_filename(form.image.data.filename)
        saveFile(form.image.data, filename)

        item = Item(name=form.name.data,
                    country=form.country.data,
                    description=form.description.data,
                    location=form.location.data,
                    image=filename,
                    image_alt = form.image_alt.data)
        item.category_id=form.category.data
        item.user_id = current_user.id

        db.session.add(item)
        db.session.commit()
        flash('The destination was successfully created.', "success")
        return redirect(url_for('home'))
    return render_template('newItem.html', form=form)



@app.route('/destination/<int:item_id>/')
def showItem(item_id):
    item = Item.query.get_or_404(item_id)

    canEdit = False
    permission = Permission(UserNeed(item.user_id))
    if permission.can():
        canEdit = True
    
    relatedItems = Item.query.options(defer("description")).filter(
                        and_(Item.country.ilike(item.country),
                             Item.id != item.id)).order_by(
                                Item.id.desc()).limit(4).all()
    return render_template('showItem.html', item=item,
                           relatedItems=relatedItems, canEdit=canEdit)



@app.route('/destination/<int:item_id>/edit/', methods=['GET', 'POST'])
#@login_required
def editItem(item_id):
    item = Item.query.get_or_404(item_id)

    permission = Permission(UserNeed(item.user_id))
    if permission.can():
        form = ItemForm(CombinedMultiDict((request.files, request.form)), obj=item)
        form.category.choices = getChoicesOfCategorySelect()
        form.image.default = item.image
        if request.method == 'GET':
            form.category.default = item.category_id
            form.category.process([])
        elif form.validate():
            if isinstance(form.image.data, FileStorage) and form.image.data:
                filename = secure_filename(form.image.data.filename)
                removeFile(item.image)
                saveFile(form.image.data, filename)
                item.image = filename
            
            item.name = form.name.data
            item.category_id = form.category.data
            item.coutry = form.country.data
            item.description = form.description.data
            item.location = form.location.data
            item.image_alt = form.image_alt.data
            db.session.add(item)
            db.session.commit()
            flash('The destination was successfully updated.', "success")
            return redirect(url_for('showItem', item_id=item.id))
        return render_template('editItem.html', form=form, item=item)
    else:
        abort(403)



@app.route('/destination/<int:item_id>/delete/', methods=['POST'])
#@login_required
def deleteItem(item_id):
    item = Item.query.get_or_404(item_id)

    permission = Permission(UserNeed(item.user_id))
    if permission.can():
        removeFile(item.image)
        db.session.delete(item)
        db.session.commit()
        flash('The destination was successfully deleted.', "success")
        return redirect(url_for('home'))
    else:
        abort(403)

    

@app.route('/categories/')
#@login_required
#@admin_permission.require(http_exception=403)
def listCategories():
    cats = Category.query.all()
    return render_template('categories.html', categories=cats)



@app.route('/category/new/', methods=['GET', 'POST'])
#@login_required
#@admin_permission.require(http_exception=403)
def newCategory():
    form = CategoryForm(request.form)
    if form.validate_on_submit():
        cat = Category(form.name.data, form.description.data)
        db.session.add(cat)
        db.session.commit()
        flash('The category was successfully created.', "success")
        return redirect(url_for('listCategories'))
    return render_template('newCategory.html', form=form)



@app.route('/category/<int:category_id>/edit/', methods=['GET', 'POST'])
#@login_required
#@admin_permission.require(http_exception=403)
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



@app.route('/category/<int:category_id>/delete/', methods=['POST'])
#@login_required
#@admin_permission.require(http_exception=403)
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



@app.route('/category/<int:category_id>')
def listItemsByCategory(category_id):
    items = Item.query.options(defer("description")).filter(
                Item.category_id == category_id).order_by(Item.id.desc()).all()
    categories = Category.query.all()
    return render_template("items.html", items=items, categories=categories)



@app.route('/category')
def searchItems():
    search_term = request.args.get('search', '')

    items = []
    if search_term:
        items = Item.query.options(defer("description")).filter(    
                    or_(Item.country.ilike("%" + search_term + "%"),
                        Item.name.ilike("%" + search_term + "%"))).order_by(
                            Item.id.desc()).all()

    categories = Category.query.all()
    return render_template("items.html", items=items, categories=categories)



@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).one()
        login_user(user)
        identity_changed.send(current_app._get_current_object(),
                              identity=Identity(user.id))

        flash('Logged in successfully.', 'success')

        return redirect(url_for('home'))
    return render_template('login.html', form=form)



@app.route("/logout/")
@login_required
def logout():
    logout_user()

    identity_changed.send(current_app._get_current_object(),
                          identity=AnonymousIdentity())

    flash("You have been logged out.", "success")
    return redirect(url_for('home'))
