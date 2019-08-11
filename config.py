import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    APP_ID = "wx37ee59c948764806"
    APP_SECRET = "ed7a0dd00407208f2f596097cc4a73e3"
    APP_TOKEN = "487529QWE"
    SECRET_KEY = '!@#$%12345'
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')


config_dict = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
