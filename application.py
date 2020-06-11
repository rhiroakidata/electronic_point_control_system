# -*- coding: utf-8 -*-

from os import getenv
from os.path import dirname, isfile, join


from dotenv import load_dotenv

from apps import create_app

# Add .env to path
_ENV_FILE = join(dirname(__file__), '.env')

# Read _ENV_FILE if exists
if isfile(_ENV_FILE):
    load_dotenv(dotenv_path=_ENV_FILE)

# Instance factory function
app = create_app(getenv('FLASK_ENV') or 'default')

if __name__ == '__main__':
    ip = '0.0.0.0'
    port = app.config['APP_PORT']
    debug = app.config['DEBUG']

    # Execute Flask web server
    app.run(
        host=ip, debug=debug, port=port, use_reloader=debug
    )
