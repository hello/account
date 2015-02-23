import os
from jinja2 import Environment, FileSystemLoader
import mandrill
import logging
from app import app

logger = logging.getLogger(__name__)

def send_reset_password(email, name, link):
   env = Environment(loader=FileSystemLoader(os.path.dirname(__file__) + '/templates/emails/'))
   subject = 'Reset your password'
   html_template = env.get_template('reset.html')
   text_template = env.get_template('reset.txt')

   html = html_template.render(subject=subject, name=name, link=link)
   text = text_template.render(subject=subject, name=name, link=link)

   send_message(email, subject, name, ['password_reset'], html, text)

def send_message(email, subject, name, tags, html, text):
    try:
        mandrill_client = mandrill.Mandrill(app.config['MANDRILL_API_KEY'])

        message = {
            'auto_html': None,
            'auto_text': None,
            #'bcc_address': 'message.bcc_address@example.com',
            'from_email': 'support@hello.is',
            'from_name': 'Hello',
            'global_merge_vars': [
                {
                    'content': 'merge1 content',
                    'name': 'merge1'
                }
                ],
            'google_analytics_campaign': 'support@hello.is',
            'google_analytics_domains': ['hello.is'],
            'headers': {
                'Reply-To': 'support@hello.is'
                },
            'html': html,
            """'images': [
                {
                    'content': 'ZXhhbXBsZSBmaWxl',
                    'name': 'IMAGECID',
                    'type': 'image/png'
                    }
                ],"""
            'important': False,
            'inline_css': True,
            'metadata': {'website': 'hello.is'},
            'preserve_recipients': None,
            'recipient_metadata': [
                {
                    'rcpt': email,

                    }
                ],
            'return_path_domain': None,
            'signing_domain': None,
            'subject': subject,
            'tags': tags,
            'text': text,
            'to': [
                {
                    'email': email,
                    'name': name,
                    'type': 'to'
                    }
            ],
            'track_clicks': None,
            'track_opens': None,
            'tracking_domain': None,
            'url_strip_qs': None,
            'view_content_link': None
        }
        result = mandrill_client.messages.send(message=message, async=False, ip_pool='Main Pool')
    except mandrill.Error, e:
        logging.error('A mandrill error occurred: %s - %s', e.__class__, e)
        raise