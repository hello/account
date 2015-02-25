class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    API_URL = 'http://localhost:9999/v1/password_reset'
    OAUTH_TOKEN = '16.b922fd625e69a49d7691cd6562b29f67'


class ProductionConfig(Config):
    DEBUG = False
    API_URL = 'https://api.hello.is/v1/password_reset'
    OAUTH_TOKEN = '6.4b2ff43787615997ac6bc055888e22ed'

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    API_URL = 'https://dev-api.hello.is/v1/password_reset'
    OAUTH_TOKEN = '18.87dd783307e7ecd22e430575cd159148'

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True