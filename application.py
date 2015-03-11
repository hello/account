from app import application
import os
if __name__ == '__main__':
    port = int(os.environ['PORT'])
    application.run(host='0.0.0.0',debug=application.config['DEBUG'], port=port)