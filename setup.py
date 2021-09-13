#
# This file is part of BDC-Auth-Client.
# Copyright (C) 2020 INPE.
#
# BDC-Auth-Client is a free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""BDC-Auth-Client is a client package for authentication and authorization based on OAuth 2.0."""

import os

from setuptools import find_packages, setup

readme = open('README.rst').read()

history = open('CHANGES.rst').read()

docs_require = [
    'Sphinx>=2.2',
    'sphinx_rtd_theme',
    'sphinx-copybutton',
]

tests_require = [
    'coverage>=4.5',
    'coveralls>=1.8',
    'pytest>=5.2',
    'pytest-cov>=2.8',
    'pytest-pep8>=1.0',
    'pydocstyle>=4.0',
    'isort>4.3',
    'check-manifest>=0.40',
    'requests-mock>=1.7'
]

extras_require = {
    'docs': docs_require,
    'tests': tests_require,
}

extras_require['all'] = [req for _, reqs in extras_require.items()
                         for req in reqs]

setup_requires = [
    'pytest-runner>=5.2',
]

install_requires = [
    'cacheout>=0.11,<1',
    'Flask>=1.1',
    'Authlib>=0.14',
    'requests>=2.20',
]

packages = find_packages()

g = {}
with open(os.path.join('bdc_auth_client', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='bdc-auth-client',
    version=version,
    description=__doc__,
    long_description=readme + '\n\n' + history,
    keywords=['user authentication', 'authorization system', 'OAuth 2.0'],
    license='MIT',
    author='Brazil Data Cube Team',
    author_email='brazildatacube@inpe.br',
    url='https://github.com/brazil-data-cube/bdc-auth-client',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    entry_points={
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
