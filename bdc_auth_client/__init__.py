#
# This file is part of BDC-Auth-Client.
# Copyright (C) 2020 INPE.
#
# BDC-Auth-Client is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""User authentication and authorization system for BDC."""

from .decorators import oauth2
from .version import __version__

__all__ = (
    'oauth2',
    '__version__',
)
