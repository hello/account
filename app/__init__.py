from flask import Flask
import os
from flask.ext.uuid import FlaskUUID

application = Flask(__name__)
FlaskUUID(application)
application.config.from_object(os.environ['APP_SETTINGS'])

from app import views
from app import config