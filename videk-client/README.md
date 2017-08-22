# videk-client package

Boot scripts for Videk client. This package provides Videk REST client and a systemd service for registration of SNA-LGTC boards in Videk management system.

To build Debian package:

    $ dpkg-buildpackage -b -uc

When built, install the package with:

    $ sudo dpkg -i videk-client_1.1.0-1_all.deb
