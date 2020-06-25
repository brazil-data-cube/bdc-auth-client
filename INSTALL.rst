..
    This file is part of BDC-Auth-Client.
    Copyright (C) 2019-2020 INPE.

    BDC-Auth-Client is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.


Installation
============


Development Installation
------------------------


Clone the software repository:


.. code-block:: shell

    git clone https://github.com/brazil-data-cube/bdc-auth-client.git


Go to the source code folder:


.. code-block:: shell

    cd bdc-auth-client


Install in development mode:


.. code-block:: shell

     pip3 install -e .[all]


Generate the documentation:


.. code-block:: shell

    python setup.py build_sphinx


The above command will generate the documentation in HTML and it will place it under::

    docs/sphinx/_build/html/

