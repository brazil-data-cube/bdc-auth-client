#
# This file is part of BDC-Auth-Client.
# Copyright (C) 2019-2020 INPE.
#
# BDC-Auth-Client is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Decorators used to integrate with BDC-Auth Provider."""

from functools import wraps

import requests
from authlib.integrations.requests_client import OAuth2Session
from authlib.oauth2.rfc6749 import ClientAuthentication
from flask import abort, current_app, request

from cacheout.cache import Cache

# Define a InMemory cache for development purporse
# Used to prevent `fetch_token` all the time.
token_cache = Cache(maxsize=512, ttl=3600)


def oauth2(roles=None, required=True):
    """Decorate a Flask route to connect with BDC-Auth Provider.

    You can specify user roles required to access a resource.

    Make sure to set the following variables to the app:

    - ``BDC_AUTH_CLIENT_ID``: Application Client Id
    - ``BDC_AUTH_CLIENT_SECRET``: Application Client Secret
    - ``BDC_AUTH_ACCESS_TOKEN_URL``: URL to BDC-Auth Provider Token

    Example:
        >>> from bdc_auth_client.decorators import oauth2
        >>>
        >>> @app.route('/')
        >>> @oauth2(roles=['admin'])
        >>> def protected_route(roles=[]):
        ...     return dict(status=200)
    """
    def _oauth2(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            access_token = request.args.get('access_token')
            if not access_token:
                if required:
                    abort(400, 'Missing access_token parameter.')
                return func(*args, **kwargs)

            if not token_cache.has(access_token):
                session = OAuth2Session(
                    client_id=current_app.config['BDC_AUTH_CLIENT_ID'],
                    client_secret=current_app.config['BDC_AUTH_CLIENT_SECRET'],
                    token_endpoint_auth_method='client_secret_basic',
                )
                try:
                    # Set policy to access the `BDC-Auth`
                    # A policy is associated with Roles.
                    policy = None

                    if roles:
                        policy = ','.join(roles)

                    res = session.fetch_token(
                        current_app.config['BDC_AUTH_ACCESS_TOKEN_URL'], grant_type='introspect',
                        token=access_token, policy=policy
                    )

                    if 'code' in res:
                        abort(403)

                    kwargs.update(dict(roles=res['sub']['roles']))
                    kwargs.update(dict(access_token=access_token))
                    if roles:
                        user_roles = res['sub']['roles'] or []

                        if not set(roles) <= set(user_roles):
                            abort(403)

                    token_cache.add(access_token, res, ttl=60)
                except Exception as e:
                    abort(403)
            return func(*args, **kwargs)
        return wrapped
    return _oauth2
