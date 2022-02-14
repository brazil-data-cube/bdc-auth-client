..
    This file is part of BDC-Auth-Client.
    Copyright (C) 2022 INPE.

    BDC-Auth-Client is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.


Using BDC-Auth-App
==================

This modules uses `Authlib <https://docs.authlib.org/en/latest/index.html>`_ implementation to communicate with Brazil Data Cube OAuth2.
You can also use this module for others OAuth 2.0 server as is.


In order to integrate your application with OAuth 2 server, you need to configure the following variables:


- ``BDC_AUTH_CLIENT_ID``: The OAuth 2 client application id.

- ``BDC_AUTH_CLIENT_SECRET``: The OAuth 2 client application secret.

- ``BDC_AUTH_ACCESS_TOKEN_URL``: The OAuth 2 server URL.


After that, the ``bdc-auth-client`` usages works as following::

    from bdc_auth_client import oauth2
    from flask import Flask

    app = Flask(__name__)
    app.config['BDC_AUTH_CLIENT_ID'] = 'ClientIdHere'
    app.config['BDC_AUTH_CLIENT_SECRET'] = 'ClientSecretHere'
    app.config['BDC_AUTH_ACCESS_TOKEN_URL'] = 'OAuth2URLHere'

    @oauth2(required=True)
    @app.route('/')
    def index(roles=None):
        return "Protected resource, you must have user to access this."

    if __name__ == '__main__':
        app.run()


Basically the :meth:`bdc_auth_client.decorators.oauth2` supports the following parameters:

- ``required``: Determines if the decorated resource must prevent any access. Default is `True`.

- ``roles``: List of roles of Authenticated User. Default is ``[]``.
