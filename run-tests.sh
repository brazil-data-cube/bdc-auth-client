#!/usr/bin/env bash
#
# This file is part of BDC-Auth-Client.
# Copyright (C) 2022 INPE.
#
# BDC-Auth-Client is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

pydocstyle bdc_auth_client setup.py && \
isort bdc_auth_client setup.py --check-only --diff && \
check-manifest --ignore ".drone.yml,.readthedocs.yml" && \
sphinx-build -qnW --color -b doctest docs/sphinx/ docs/sphinx/_build/doctest #&& \
pytest