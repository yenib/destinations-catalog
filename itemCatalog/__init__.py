import os
from itemCatalog.config import config

from flask import Flask




app = Flask(__name__)

config_name = os.getenv('ITEMCATALOG_CONFIG', 'development')
app.config.from_object(config[config_name])







import itemCatalog.views
