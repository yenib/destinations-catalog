from itemCatalog import app
from flask import render_template


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
    return "List of categories goes here."


@app.route('/category/new/')
def newCategory():
    return "New Category goes here."


@app.route('/category/<int:category_id>/edit')
def editCategory(category_id):
    return "Edit Category goes here."


@app.route('/category/<int:category_id>/delete')
def deleteCategory(category_id):
    return "Delete Category goes here."

