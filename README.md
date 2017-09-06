# SNA-LGTC

![Photo of the SNA-LGTC board](figures/sna-lgtc.jpg)

SNA-LGTC is a small, ARM-based Linux-running computer that is capable of hosting
microcontroller-based boards such as VESNA SNC and VESNA SNP. This repository
contains various small software parts and documentarion related to
SNA-LGTC:

 * `dts` - Device tree source and compiled device tree blobs.
 * `docker` - Configuration for Docker.
 * `figures` - Photos and other figures related to the SNA-LGTC board.
 * `munin` - Munin plugins.

It also contains sources for several Debian packages that need to be installed
on SNA-LGTC boards:

 * `bb-wl18xx-firmware` - Customized WL1837 firmware and related scripts.
 * `sna-lgtc-boot` - First boot setup scripts for setting up hostname, machine
   ID, etc.
 * `vesna-snc-boot` - Systemd service that boots the VESNA SNC guest board
   after the host boots.
 * `videk-client` - Client for the Videk management system.

Related repositories and documents in other places:

 * [Schematic and PCB layout](https://github.com/urbangregorc/vesna-hardware/tree/SNA-LGTC/SNA-LGTC/v1.1.0) for the SNA-LGTC board.
 * [Patched OpenOCD](https://github.com/avian2/openocd/tree/sna-lgtc) for programming the guest VESNA SNC board.
 * [Instructions](https://github.com/avian2/vesna-drivers/blob/logatec-3/README.beaglebone.md)
   for compiling, uploading and debugging firmware for the guest VESNA SNC
   board using *vesna-drivers* from the host SNA-LGTC board.
 * [NodeSpectrumSensorLocal](https://github.com/avian2/vesna-drivers/tree/logatec-3/Applications/Logatec/NodeSpectrumSensorLocal), application for controlling the SNE-ISMTV radio on the guest board using ALH protocol over the UART.
 * [VESNA management system](https://github.com/matevzv/vesna-management-system), web application for remote access over ALH to the guest VESNA SNC.
 * [Boot scripts](https://github.com/avian2/bone-boot-scripts/tree/sna-lgtc), customized BeagleBone boot scripts for SNA-LGTC.
 * [Logatec temperature monitor](https://github.com/avian2/logatec-temp-monitor), a containerized temperature monitoring application for SNA-LGTC.

## Connectors

The board will boot when one of the connectors providing power supply is
connected (230V AC, 12V DC or the 5V supply from the USB gadget).

To start, connect mini-USB cable to the USB gadget connector, bring up the USB
network interface using DHCP and log in to 192.168.7.2 over *ssh*. In this
case, no other power supply is needed.

It is also possible to log in and work over the serial console. In this case,
connect a mini-USB cable to the USB console connector and also connect another
power supply (either 230V AC, 12V DC or 5V to the USB gadget).

If you can connect only one antenna for Wi-Fi, use connector J4. If possible,
connect both antennas.

![Annotated connectors on the SNA-LGTC board](figures/connectors.png)

## LEDs

In normal operation, green power LED should be lit and the blue heartbeat LED
should be blinking periodically.

![Annotated LEDs on the SNA-LGTC board](figures/leds.png)

## Buttons

On its own, the board will boot from the SD card if it appears bootable (for
example, if it contains a `/boot/uEnv.txt` file). If the SD card does not
appear to be bootable, it will boot from the internal eMMC flash.

Pressing the *Power* button has the same effect as running `shutdown -h now`.
In other words, it will gracefully stop the system and power off the board.

The *Reset* button however hard-reboots the board. It does not perform a
graceful shutdown and hence using it carries the risk of filesystem corruption.

![Annotated buttons on the SNA-LGTC board](figures/buttons.png)
