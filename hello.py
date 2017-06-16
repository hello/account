import requests
from requests import ConnectionError
import json
import logging

logger = logging.getLogger(__name__)

class ApiClient(object):
    def __init__(self, endpoint, oauth_token):
        self.endpoint = endpoint
        self.headers = headers={'Content-Type' : 'application/json', 'Authorization' : 'Bearer %s' % oauth_token}

    def send_email(self, email):    
        url = "%spassword_reset/" % self.endpoint
        try:
            r = requests.post(url, data=json.dumps({'email' : email.lower()}), headers=self.headers)
        except ConnectionError, e:
            logging.error(e)

        return True

    def validate_link(self, uuid, state):
        url = "%spassword_reset/%s/%s" % (self.endpoint, uuid, state)
        logging.info("url: %s", url)
        try:
            r = requests.get(url, headers=self.headers)
            logging.info("status code: %d", r.status_code)
            # api does not return a response here
            return r.status_code == 204
        except ConnectionError, e:
            logging.error(e)
        logging.info("has expired")
        return False

    def update(self, uuid, state, password):
        url = "%spassword_reset/update" % self.endpoint
        data = {'uuid' : str(uuid), 'state' : state, 'password' : password}
        try:
            r = requests.post(url, data=json.dumps(data), headers=self.headers)
            if r.status_code in [204, 200]:
                logging.info("Password successfully updated")
                return True
            logging.error("HTTP:%d - %s", r.status_code, r.content)
        except ConnectionError, e:
            logging.error(e)

        return False

    def export(self, uuid):
        url = "%sexport_data/%s" % (self.endpoint, uuid)
        print url
        try:
            r = requests.post(url, data={}, headers=self.headers)
            if r.status_code in [204, 200, 404]:
                logging.info("Export data trigger successful")
                return True
            logging.error("HTTP:%d - %s", r.status_code, r.content)
        except ConnectionError, e:
            logging.error(e)

        return False        

