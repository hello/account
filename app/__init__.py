from flask import Flask
import os
from flask.ext.uuid import FlaskUUID

app = Flask(__name__)
FlaskUUID(app)
app.config.from_object(os.environ['APP_SETTINGS'])

from app import views
from app import config