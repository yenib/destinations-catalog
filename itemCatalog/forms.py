from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, Optional, Length, ValidationError 

from itemCatalog.models import Category



class CategoryForm(FlaskForm):
    name = StringField('Name', [InputRequired(), Length(max=80)])
    description = TextAreaField('Description', [Optional()])

    def validate_name(form, field):
        if field.data != field.default:
            cat = Category.query.filter(Category.name.ilike(field.data)).first()
            if cat:
                raise ValidationError('A category with this name already exists.')
