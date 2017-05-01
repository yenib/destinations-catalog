from itemCatalog import db
from itemCatalog.models import User

from flask import current_app
from flask_login.utils import login_user
from flask_principal import identity_changed, Identity

import hashlib
import os


def getAntiForgeryToken():
    token = hashlib.sha256(os.urandom(1024)).hexdigest()
    return token



def createOrSignInUser(email, password="", name="", lastName="",
                       picture="", active=True):
    
    user = User.query.filter_by(email=email).first()

    # Add user to DB if not exist
    if not user:
        password = getAntiForgeryToken() #TODO: hash password
        user = User(email, password)
        user.name = name
        user.last_name = lastName
        user.picture = picture
        user.active = active
        db.session.add(user)
        db.session.commit()
    
    login_user(user)
    identity_changed.send(current_app._get_current_object(),
                          identity=Identity(user.id))
    
    return user
