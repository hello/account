import requests
from app import app
from flask import Flask, render_template, redirect, request, url_for
from requests import ConnectionError
from wtforms import Form, BooleanField, TextField, PasswordField, validators

import logging
import json
from hello import ApiClient

logger = logging.getLogger(__name__)

apiClient = ApiClient(app.config['API_URL'], app.config['OAUTH_TOKEN'])

@app.route('/reset', methods=['GET', 'POST'])
def register():
    form = ResetForm(request.form)
    error_message = ''
    if request.method == 'POST' and form.validate():
        resp = apiClient.send_email(form.email.data)
        if resp:
            return render_template('reset_success.html')
            
        error_message = 'Something went wrong, please try again.'

    return render_template('reset.html', form=form, error_message=error_message)


@app.route('/success', methods=['GET'])
def success():
    return render_template('update_success.html')

@app.route('/error', methods=['GET'])
def error():
    return render_template('update_error.html'), 500


@app.route('/password_update/<uuid:id>/<state>', methods=['GET', 'POST'])
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