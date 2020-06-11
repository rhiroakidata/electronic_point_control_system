# -*- coding: utf-8 -*-

# Python
from os.path import dirname, isfile, join

import pytest
from dotenv import load_dotenv

from apps import create_app

# Add .env to path
_ENV_FILE = join(dirname(__file__), '../.env')

# Read _ENV_FILE if exists
if isfile(_ENV_FILE):
    load_dotenv(dotenv_path=_ENV_FILE)


# When use command pytest, create a fixture
@pytest.fixture(scope='session')
def client():

    # Instance factory function
    flask_app = create_app('testing')

    # Fuction to test web app and manage settings using Werkzeug test client
    testing_client = flask_app.test_client()

    # Create context with application settings
    ctx = flask_app.app_context()
    ctx.push()

    # return client created
    yield testing_client

    # remove context after test
    ctx.pop()


@pytest.fixture(scope='function')
def mongo(request, client):

    def fin():
        print('\n[teardown] disconnect from db')

    fin()
