class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    API_URL = 'http://localhost:9999/v1/'
    OAUTH_TOKEN = '3.81e6a3ee26454d62807f90295e383359'


class ProductionConfig(Config):
    DEBUG = False
    API_URL = 'https://api.hello.is/v1/'
    OAUTH_TOKEN = '6.4b2ff43787615997ac6bc055888e22ed'


class StagingConfig(Config):
    DEBUG = True
    API_URL = 'https://dev-api.hello.is/v1/'
    OAUTH_TOKEN = '18.b7a93325d5824901a0408d3682153b1f'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
