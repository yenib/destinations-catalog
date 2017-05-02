from flask_restful import fields

from flask import url_for


# What does this file do?
#  - defines for each model entity used what data will be provided through
#    the Application's API endpoints


category_nested_items_fields = {
    'id': fields.Integer,
    'name': fields.String
}



categoryFields = {
    'id': fields.Integer(),
    'name': fields.String(),
    'description': fields.String(),
    'items': fields.List(fields.Nested(category_nested_items_fields))
}



class ImageDownloadUrl(fields.Raw):
    def format(self, value):
        return url_for('downloadFile', filename=value, _external=True)




itemFields = {
    'id': fields.Integer(),
    'name': fields.String(),
    'description': fields.String(),
    'image': ImageDownloadUrl(),
    'image_alt': fields.String(),
    'country': fields.String(),
    'location': fields.String(),
    'category_id': fields.Integer()
}
