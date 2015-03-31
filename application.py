
import os
from flask.ext.uuid import FlaskUUID
import config
import requests
from flask import Flask, render_template, redirect, request, url_for
from requests import ConnectionError
from wtforms import Form, BooleanField, TextField, PasswordField, validators

import logging
import json
from hello import ApiClient
from flask_sslify import SSLify


application = Flask(__name__)
FlaskUUID(application)
sslify = SSLify(app)

application.config.from_object(os.environ['APP_SETTINGS'])

logger = logging.getLogger(__name__)

apiClient = ApiClient(application.config['API_URL'], application.config['OAUTH_TOKEN'])

@application.route('/', methods=['GET'])
def home():
    return redirect(url_for('register'))

@application.route('/reset', methods=['GET', 'POST'])
def register():
    form = ResetForm(request.form)
    error_message = ''
    if request.method == 'POST' and form.validate():
        resp = apiClient.send_email(form.email.data)
        if resp:
            return render_template('reset_success.html', user_email=form.email.data)
            
        error_message = 'Something went wrong, please try again.'

    return render_template('reset.html', form=form, error_message=error_message)


@application.route('/success', methods=['GET'])
def success():
    return render_template('update_success.html')

@application.route('/error', methods=['GET'])
def error():
    return render_template('update_error.html'), 500


@application.route('/password_update/<uuid:id>/<state>', methods=['GET', 'POST'])
def updatePassword(id, state):
    link_is_valid = apiClient.validate_link(id, state)
    if not link_is_valid:
        return render_template('expired.html')

    form = UpdatePasswordForm(request.form)
    if request.method == 'POST' and form.validate():
        if apiClient.update(id, state, form.password.data):
            return redirect(url_for('success'))
        else:
            return redirect(url_for('error'))
    return render_template('update.html', id=id, state=state, form=form)


class ResetForm(Form):
    email =  TextField('Email address', [validators.Email(message="Email address is not valid.")])

class UpdatePasswordForm(Form):
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')

if __name__ == '__main__':
    #port = int(os.environ['PORT'])
    application.run(host='0.0.0.0',debug=application.config['DEBUG'])
