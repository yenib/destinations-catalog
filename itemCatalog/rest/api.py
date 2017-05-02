from flask_restful import Resource, marshal_with

from itemCatalog.models import Category, Item
from itemCatalog.rest.fields import categoryFields, itemFields


# What does this file do?
#  - defines the API endpoints of the Application




class CategoryAPI(Resource):

    # endpoint to query all categories or a specific category
    @marshal_with(categoryFields)
    def get(self, category_id=None):
        if category_id:
            return Category.query.get_or_404(category_id)
        else:
            return Category.query.all()



class ItemAPI(Resource):

    # endpoint to query all destinations or a specific destination
    @marshal_with(itemFields)
    def get(self, item_id=None):
        if item_id:
            return Item.query.get_or_404(item_id)
        else:
            return Item.query.all()
        
