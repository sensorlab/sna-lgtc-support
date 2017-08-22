# SNA-LGTC-boot package

This package provides scripts and a systemd service for proper initialization of SNA-LGTC board. It has two parts: The first part runs only on first boot and the second part runs on each boot. The first part sets machine_id and formats the SD card and the second part sets the hostname based on the IP address.

To build Debian package:

    $ dpkg-buildpackage -b -uc

When built, install the package with:

    $ sudo dpkg -i sna-lgtc-boot_1.1.0-1_all.deb
