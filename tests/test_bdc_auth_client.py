#
# This file is part of BDC-Auth-Client.
# Copyright (C) 2021 INPE.
#
# BDC-Auth-Client is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Unit-test for BDC-Auth-Client."""

from flask import Flask
from werkzeug.exceptions import HTTPException, InternalServerError

from bdc_auth_client.decorators import oauth2


TOKEN = 'Fake'
ROUTE = '/'
HOST = 'https://localhost'


def setup_app(throw_exception=True, required=True):
    """Create a Flask application with a minimal routes and testing purposes."""
    app = Flask(__name__)
    app.config['BDC_AUTH_ACCESS_TOKEN_URL'] = HOST
    app.config['BDC_AUTH_CLIENT_ID'] = ''
    app.config['BDC_AUTH_CLIENT_SECRET'] = ''

    @app.route(ROUTE)
    @oauth2(roles=['admin'], throw_exception=throw_exception, required=required)
    def index(**kwargs):
        """Return the protected index route."""
        return dict(msg='OK')

    @app.errorhandler(Exception)
    def handle_exception(e):
        """Handle exceptions."""
        if isinstance(e, HTTPException):
            return {'code': e.code, 'description': e.description}, e.code

        app.logger.exception(e)

        return {'code': InternalServerError.code,
                'description': InternalServerError.description}, InternalServerError.code

    return app


def assert_json(response, code, msg=None):
    """Define a assert utility for JSON API responses."""
    assert response.content_type == 'application/json'
    assert response.status_code == code
    if msg:
        assert response.json['code'] == code
        assert response.json['description'] == msg


def get_app_client(**options):
    """Wrap the flask application and return a test client."""
    app = setup_app(**options)

    return app.test_client()


def test_decorator_token_expired(requests_mock):
    """Test the token expiration and message."""
    client = get_app_client()

    # Token Expired
    requests_mock.post(HOST, json=dict(status=False),
                       status_code=200,
                       headers={'content-type': 'application/json'})
    resp = client.get(ROUTE, query_string=dict(access_token=TOKEN))
    assert_json(resp, 401, 'Token expired.')


def test_decorator_forbidden(requests_mock):
    """Test the default behavior for decorator (User without right permission)."""
    client = get_app_client()

    requests_mock.post(HOST, json=dict(status=True, sub=dict(roles=['read'])),
                       status_code=200,
                       headers={'content-type': 'application/json'})
    resp = client.get(ROUTE, query_string=dict(access_token=TOKEN))
    assert_json(resp, 403, 'You don\'t have permission to access this resource.')


def test_decorator_missing_token(requests_mock):
    client = get_app_client()

    # Missing TOKEN (Required)
    requests_mock.post(HOST, json=dict(status=True, sub=dict(roles=['admin'])),
                       status_code=200,
                       headers={'content-type': 'application/json'})
    resp = client.get(ROUTE)
    assert_json(resp, 401, 'Missing access_token parameter.')


def test_token_optional(requests_mock):
    client_non_required = get_app_client(required=False)
    # Missing TOKEN (non-required)
    requests_mock.post(HOST, json=dict(status=True, sub=dict(roles=['admin'])),
                       status_code=200,
                       headers={'content-type': 'application/json'})
    resp = client_non_required.get(ROUTE)
    assert_json(resp, 200)
    assert resp.json['msg'] == 'OK'


def test_remote_server_internal_error(requests_mock):
    client = get_app_client()

    expected_code = 500
    expected_msg = InternalServerError.description

    # Token OK
    requests_mock.post(HOST, json=dict(),
                       status_code=expected_code,
                       headers={'content-type': 'application/json'})
    resp = client.get(ROUTE, query_string=dict(access_token=TOKEN))

    assert_json(resp, expected_code, expected_msg)


def test_decorator(requests_mock):
    client = get_app_client()

    # Token OK
    requests_mock.post(HOST, json=dict(status=True, sub=dict(roles=['admin'])),
                       status_code=200,
                       headers={'content-type': 'application/json'})
    resp = client.get(ROUTE, query_string=dict(access_token=TOKEN))
    assert_json(resp, 200)
    assert resp.json['msg'] == 'OK'

    # Test again to use cache
    resp = client.get(ROUTE, query_string=dict(access_token=TOKEN))
    assert_json(resp, 200)
