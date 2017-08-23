# SNA-LGTC-boot package

This package provides scripts and a Systemd service for initialization of the
SNA-LGTC board. It has two parts:

 * The first part runs only on first boot. It sets `/etc/machine-id` based on
   the MAC addresses of the two Sitara Ethernet interfaces and the wireless LAN
   interface. It also formats the SD card.

   First boot is detected by the presence of `/etc/lgtc/lgtc-first-boot` file.
   This file is created by the eMMC flasher script when the eMMC is programmed
   from the SD card.

 * The second part runs on each boot. It sets the hostname based on the IP
   address of the wireless LAN interface.

To build Debian package:

    $ dpkg-buildpackage -b -uc

When built, install the package with:

    $ sudo dpkg -i sna-lgtc-boot_1.1.0-1_all.deb

Note that a lot of board initialization tasks that are identical (or almost
identical) to the BeagleBone boards are performed by the customized [BeagleBone
Boot scripts](https://github.com/avian2/bone-boot-scripts/tree/sna-lgtc).
