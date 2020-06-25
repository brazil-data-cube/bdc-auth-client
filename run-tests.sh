#!/usr/bin/env bash
#
# This file is part of BDC-Auth-Client.
# Copyright (C) 2019-2020 INPE.
#
# BDC-Auth-Client is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

pydocstyle bdc_auth_client && \
isort --check-only --diff --recursive **/*.py && \
check-manifest --ignore ".travis-*" --ignore ".readthedocs.*" && \
python setup.py test && \
sphinx-build -qnW --color -b doctest docs/sphinx/ docs/sphinx/_build/doctest