from flask_sqlalchemy import SQLAlchemy


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
    country = db.Column(db.String(80))
    state = db.Column(db.String(80))
    city =  db.Column(db.String(80))
    category_id = db.Column(db.Integer(), db.ForeignKey("category.id"))

    def __init__(self, name, description, image=None):
        self.name = name
        self.description = description
        seld.image = image

    def __repr__(self):
        return '<Item %r>' % self.name


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    picture = db.Column(db.String(255))

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.email
