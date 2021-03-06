import os


# What does this file do?
#  - defines global application settings for different environments



class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = '\x99\xa2\xb2x?\xc0\xdc?\x1c\x83\x06\x9de\xf6\x13\xb4\n\x00\x9d1\xb9\x05\xeb\xf5'

    APP_ROOT = os.path.dirname(os.path.abspath(__file__))

    UPLOAD_FOLDER = APP_ROOT + '/../uploads'
    UPLOADS_ALLOWED_IMAGES = set(['jpg', 'jpe', 'jpeg', 'png'])
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024

    #Flask-WTF config variable
    WTF_CSRF_SECRET_KEY = 'w\x0b!\x0f\x07X\x8e\x9a3[\xf2;\xd4Q\xafMb\xce\xa0\xbd\x9a<)\x9d'


class DevConfig(Config):
    DEBUG = True
    SECRET_KEY = '\x1a\xc2@\x12\xec\xb4\xefuf\xba\xf4=\xee\xceg\xbc\xd2p\xd5q\xf1\x05\xd0\xdd'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../itemcatalog_database.db'


class ProdConfig(Config):
    SECRET_KEY = '\x1f\x99\x1c\x14v\x0f\xebyZnT\x98\xef\x8e\x83x\x90b\xd5\xea\x93\xfc\x04\xf1'
    # Sets URI for production DB. Heroku creates the DATABASE_URL environment
    # variable when the Postgres addon is added to our Heroku app.
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')    
    SQLALCHEMY_TRACK_MODIFICATIONS=False

    GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
    FACEBOOK_CLIENT_SECRET = os.getenv('FACEBOOK_CLIENT_SECRET')
    

class TestConfig(Config):
    TESTING = True
    SECRET_KEY = '\x08|\xbdL\xb1\xa6\x1c\xab\xe8\xdet\x95\xe2S@\xefig_\xeeXI\x96D'




config = {
    "development": "itemCatalog.config.DevConfig",
    "testing": "itemCatalog.config.TestConfig",
    "production": "itemCatalog.config.ProdConfig"
}    
