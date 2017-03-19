import os

from flask import Flask

from itemCatalog.config import config
from itemCatalog.models import db



app = Flask(__name__)

config_name = os.getenv('ITEMCATALOG_CONFIG', 'development')
app.config.from_object(config[config_name])


db.init_app(app)

#with app.app_context():
#    db.create_all()




import itemCatalog.views
