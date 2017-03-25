from flask_sqlalchemy import SQLAlchemy

from flask_login.mixins import AnonymousUserMixin


db = SQLAlchemy()



class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text())
    items = db.relationship('Item', backref = "category", lazy = "dynamic")

    def __init__(self, name, description=None):
        self.name = name
        self.description = description


    def __repr__(self):
        return '<Category %r>' % self.name


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    description = db.Column(db.Text())
    image = db.Column(db.String(255))
    imageAlt = db.Column(db.String(150))
    country = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(150))
    categoryId = db.Column(db.Integer(),
                            db.ForeignKey("category.id"),
                            nullable=False)
    userId = db.Column(db.Integer(),
                            db.ForeignKey("user.id"),
                            nullable=False)


    def __init__(self, name, country, image="", imageAlt="",
                 description="", location=""):
        self.name = name
        self.country = country
        self.image = image
        self.imageAlt = imageAlt
        self.description = description
        self.location = location

    def __repr__(self):
        return '<Item %r>' % self.name



roles = db.Table(
    'role_users',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True)
)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    picture = db.Column(db.String(255))
    active = db.Column(db.Boolean, default=False)
    items = db.relationship('Item', backref = "user", lazy = "dynamic")
    roles = db.relationship('Role', secondary=roles,
                            backref=db.backref('users', lazy='dynamic'))

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.email


    #Flask-Login required implementations
    def is_authenticated(self):
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True

        
    def is_active(self):
        #self.active
        return True


    def is_anonymous(self):
        if isinstance(self, AnonymousUserMixin):
            return True
        else:
            return False


    def get_id(self):
        return unicode(self.id)
    #/Flask-Login required implementations




class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return '<Role %r>' % self.name     
