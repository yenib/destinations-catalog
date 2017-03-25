import os

from flask import Flask
from flask_principal import identity_loaded, RoleNeed, UserNeed
from flask_login.utils import current_user

from itemCatalog.config import config
from itemCatalog.models import db
from itemCatalog.extensions import login_manager, principals


app = Flask(__name__)

config_name = os.getenv('ITEMCATALOG_CONFIG', 'development')
app.config.from_object(config[config_name])


db.init_app(app)
login_manager.init_app(app)
principals.init_app(app)


@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    # Not needed - Add user object to the identity
    #identity.user = current_user

    # Add the UserNeed to the identity
    if getattr(current_user, 'id', None):
        identity.provides.add(UserNeed(current_user.id))

    # Add each role to the identity
    if getattr(current_user, 'roles', None):
        for role in current_user.roles:
            identity.provides.add(RoleNeed(role.name))
                

# just for development
#with app.app_context():
#    db.drop_all()
#    db.create_all()
#    import populateDB as p
#    p.populateDB(db)
    




import itemCatalog.views
