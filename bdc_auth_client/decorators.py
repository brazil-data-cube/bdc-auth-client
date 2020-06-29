#
# This file is part of BDC-Auth-Client.
# Copyright (C) 2019-2020 INPE.
#
# BDC-Auth-Client is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Decorators used """

from functools import wraps

import requests
from authlib.integrations.requests_client import OAuth2Session
from authlib.oauth2.rfc6749 import ClientAuthentication
from cacheout.cache import Cache
from flask import abort, current_app, request


# Define a InMemory cache for development purporse
# Used to prevent `fetch_token` all the time.
token_cache = Cache(maxsize=512, ttl=3600)


def oauth2_required(roles=None):
    """Simple decorator for connect with BDC-Auth Provider.

    You can specify user roles required to access a resource.

    Example:
        >>> from bdc_auth_client.decorators import oauth2_required
        >>>
        >>> @app.route('/')
        >>> @oauth2_required()
        >>> def protected_route():
        ...     return dict(status=200)
    """
    def _oauth2_required(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            access_token = request.args.get('access_token')
            if not access_token:
                abort(400, 'Missing access_token parameter.')

            if not token_cache.has(access_token):
                session = OAuth2Session(
                    client_id=current_app.config['BDC_AUTH_CLIENT_ID'],
                    client_secret=current_app.config['BDC_AUTH_CLIENT_SECRET'],
                    token_endpoint_auth_method='client_secret_basic',
                )
                try:
                    res = session.fetch_token(
                        current_app.config['BDC_AUTH_ACCESS_TOKEN_URL'], grant_type='personal_access_token', access_token=access_token)
                    if 'access_token' not in res:
                        abort(403)

                    if roles:
                        headers = dict(Authorization=f'Bearer {res["access_token"]}')
                        profile = requests.get(current_app.config['BDC_AUTH_RESOURCE_URL'],headers=headers).json()['users']

                        if profile['roles'] and not set(roles) <= set(profile['roles']):
                            abort(403)

                    token_cache.add(access_token, dict(profile=profile, access_token=res['access_token']), ttl=res['expires_in'])
                except Exception as e:
                    abort(403)
            return func(*args, **kwargs)
        return wrapped
    return _oauth2_required
