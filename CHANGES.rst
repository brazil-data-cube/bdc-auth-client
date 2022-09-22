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


Changes
=======


Version 0.4.2 (2022-09-22)
--------------------------

- Change LICENSE to GPL v3


Version 0.4.1 (2022-09-08)
--------------------------

- Fix exception when OAuth2 servers delivery a expired token (Authlib 1.0+) (`#31 <https://github.com/brazil-data-cube/bdc-auth-client/issues/31>`_)
- Update license headers date


Version 0.4.0 (2022-02-14)
--------------------------


- Improve log handler for expired tokens and generic errors `#16 <https://github.com/brazil-data-cube/bdc-auth-client/issues/16>`_.
- Improve documentation and usage `#9 <https://github.com/brazil-data-cube/bdc-auth-client/issues/9>`_.


Version 0.2.3 (2021-08-12)
--------------------------


- Add support for OR operations `#25 <https://github.com/brazil-data-cube/bdc-auth-client/issues/25>`_.

- Remove travis CI `#24 <https://github.com/brazil-data-cube/bdc-auth-client/issues/24>`_.

- Add drone support `#18 <https://github.com/brazil-data-cube/bdc-auth-client/issues/18>`_.

Version 0.2.2 (2021-07-12)
--------------------------


- Retrieve user id in decorators `#20 <https://github.com/brazil-data-cube/bdc-auth-client/issues/20>`_.


Version 0.2.1 (2022-08-26)
--------------------------


- Bug Fix in decorator oauth2: See `commit aa436 <https://github.com/brazil-data-cube/bdc-auth-client/commit/aa43602d25063678e69ba6ff6bd84653a7b20e2b>`_.



Version 0.2.0 (2022-08-20)
--------------------------


- First experimental version.
- Based on `BDC-Auth <https://github.com/brazil-data-cube/bdc-auth>`_.
- Based on OAuth 2.0 Authorization Framework - `RFC6749 <https://tools.ietf.org/html/rfc6749>`_.
- Based on `Authlib <https://authlib.org/>`_.
- Documentation system based on Sphinx.
- Package support through Setuptools.
- Installation instructions.
- Source code versioning based on `Semantic Versioning 2.0.0 <https://semver.org/>`_.
- License: `MIT <https://github.com/brazil-data-cube/bdc-auth-client/blob/master/LICENSE>`_.
