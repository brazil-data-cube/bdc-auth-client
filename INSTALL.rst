..
    This file is part of BDC-Auth-Client.
    Copyright (C) 2022 INPE.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <https://www.gnu.org/licenses/gpl-3.0.html>.


Installation
============


Development Installation
------------------------


Clone the software repository::

    git clone https://github.com/brazil-data-cube/bdc-auth-client.git


Go to the source code folder:


.. code-block:: shell

    cd bdc-auth-client


Install in development mode::

    pip3 install -e .[all]


Generate the documentation:


.. code-block:: shell

    python setup.py build_sphinx


The above command will generate the documentation in HTML and it will place it under::

    docs/sphinx/_build/html/