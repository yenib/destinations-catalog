class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = '\x99\xa2\xb2x?\xc0\xdc?\x1c\x83\x06\x9de\xf6\x13\xb4\n\x00\x9d1\xb9\x05\xeb\xf5'


class DevConfig(Config):
    DEBUG = True
    SECRET_KEY = '\x1a\xc2@\x12\xec\xb4\xefuf\xba\xf4=\xee\xceg\xbc\xd2p\xd5q\xf1\x05\xd0\xdd'


class TestConfig(Config):
    TESTING = True
    SECRET_KEY = '\x08|\xbdL\xb1\xa6\x1c\xab\xe8\xdet\x95\xe2S@\xefig_\xeeXI\x96D'




config = {
    "development": "itemCatalog.config.DevConfig",
    "testing": "itemCatalog.config.TestConfig",
    "production": "itemCatalog.config.ProdConfig"
}    
