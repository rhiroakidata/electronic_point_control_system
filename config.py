# Python 3
from os import getenv


class Config:
    SECRET_KEY = getenv('SECRET_KEY') or 'so big secret pontotel key'
    APP_PORT = int(getenv('APP_PORT', 5000))
    DEBUG = getenv('DEBUG') or False


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    MONGODB_HOST = getenv('MONGODB_URI', 'mongodb://localhost:27017/api-pontotel')


class TestingConfig(Config):
    FLASK_ENV = 'testing'
    TESTING = True
    MONGODB_HOST = getenv('MONGODB_URI_TEST', 'mongodb://localhost:27017/api-pontotel-test')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
