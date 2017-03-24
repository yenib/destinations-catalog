from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed

from wtforms import StringField, TextAreaField, SelectField, PasswordField
from wtforms.validators import InputRequired, Optional, Length, ValidationError 

from itemCatalog import app
from itemCatalog.models import Category, User



class CategoryForm(FlaskForm):
    name = StringField('Name', [InputRequired(), Length(max=80)])
    description = TextAreaField('Description', [Optional()])

    def validate_name(form, field):
        if field.data != field.default:
            cat = Category.query.filter(Category.name.ilike(field.data)).first()
            if cat:
                raise ValidationError('A category with this name already exists.')




class ItemForm(FlaskForm):
    name = StringField('Name', [InputRequired(), Length(max=120)])
    description = TextAreaField('Description', [Optional()])
    country = StringField('Country', [InputRequired(), Length(max=80)])
    location = StringField('Location', [Optional(), Length(max=150)])
    category = SelectField('Category', choices=[], coerce=int)
    image = FileField('Picture', [FileAllowed(
        app.config['UPLOADS_ALLOWED_IMAGES'],
            'Invalid image (valids: %s).' % ", ".join(
                str(ext) for ext in app.config['UPLOADS_ALLOWED_IMAGES']))])
    imageAlt = StringField('Picture Alt', [Optional(), Length(max=150)])


    def validate_category(form, field):
        if not field.data or field.data == 0:
            raise ValidationError("This field is required.")


    def validate_image(form, field):
        if not field.default:
            required = FileRequired()
            required(form, field)
                


class LoginForm(FlaskForm):
    email = StringField('Email', [InputRequired(), Length(max=120)])
    password = PasswordField('Password', [InputRequired(), Length(max=160)]) 

    def validate_email(form, field):
        user = User.query.filter_by(email=field.data).first()
        if not user or user.password != form.password.data:
            raise ValidationError('Invalid username or password.')

    
        
