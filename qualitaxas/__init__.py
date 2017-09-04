from flask import Flask, url_for
from flask_jsglue import JSGlue
from flask_mail import Mail
import boto3

app = Flask(__name__)
mail = Mail(app)
jsglue = JSGlue(app)
s3 = boto3.resource('s3')


from flask_sqlalchemy import SQLAlchemy
app.config.from_object('qualitaxas.config.DevelopmentConfig')

from qualitaxas.model import *
db = SQLAlchemy(app)
db.init_app(app)
with app.app_context():
        db.create_all()

from qualitaxas.views import view
from qualitaxas.rest_api import *

from flask_assets import Environment, Bundle
assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('styles/main.scss', filters='pyscss', output='styles/all.css')
assets.register('scss_all', scss)
assets.init_app(app)