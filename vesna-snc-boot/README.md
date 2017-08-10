This package contains a small script and a systemd service that boots up the
guest VESNA SNC board when the host SNA-LGTC board boots. It also shuts it down
when the SNA-LGTC shuts down.

More specifically, it enables the VESNA_EN pin and boots the board over JTAG
using openocd (which must be installed and properly configured - [instructions](https://github.com/avian2/vesna-drivers/blob/logatec-3/README.beaglebone.md)).

To build Debian package:

    $ dpkg-buildpackage -b -uc
