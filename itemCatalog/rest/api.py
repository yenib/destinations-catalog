from flask_restful import Resource, marshal_with

from itemCatalog.models import Category, Item
from itemCatalog.rest.fields import categoryFields, itemFields





class CategoryAPI(Resource):
    @marshal_with(categoryFields)
    def get(self, category_id=None):
        if category_id:
            return Category.query.get_or_404(category_id)
        else:
            return Category.query.all()



class ItemAPI(Resource):
    @marshal_with(itemFields)
    def get(self, item_id=None):
        if item_id:
            return Item.query.get_or_404(item_id)
        else:
            return Item.query.all()
        
