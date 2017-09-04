import os
from qualitaxas import app

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SECRET_KEY = os.environ.get('qualitaxas_secret_key', '1234567890')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    FLASKS3_USE_HTTPS = True
    MAIL_USERNAME = os.environ.get('GMAIL_EMAIL')
    MAIL_PASSWORD = os.environ.get('GMAIL_PASSWORD')
    # AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    # AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    # FLASKS3_BUCKET_NAME = os.environ.get('FLASKS3_BUCKET_NAME')
    # FLASKS3_REGION = os.environ.get('FLASKS3_REGION')
    # UPLOAD_FOLDER = '.static/'
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True
    FLASKS3_DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_RECORD_QUERIES = True




