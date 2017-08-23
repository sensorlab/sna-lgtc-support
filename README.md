# SNA-LGTC

![Photo of the SNA-LGTC board](figures/sna-lgtc.jpg)

SNA-LGTC is a small, ARM-based Linux-running computer that is capable of hosting
microcontroller-based boards such as VESNA SNC and VESNA SNP. This repository
contains various small software parts and documentarion related to
SNA-LGTC:

 * `dts` - Device tree source.
 * `dtb` - Compiled device tree blobs.
 * `wlconf` - Configuration for the TI WL1837 wi-fi module.
 * `bluetooth` - Using Bluetooth on WL1837.
 * `docker` - Configuration for Docker.
 * `figures` - Photos and other figures related to the SNA-LGTC board.

It also contains sources for several Debian packages that need to be installed
on SNA-LGTC boards:

 * `sna-lgtc-boot` - First boot setup scripts for setting up hostname, machine
   ID, etc.
 * `vesna-snc-boot` - Systemd service that boots the VESNA SNC guest board
   after the host boots.
 * `videk-client` - Client for the Videk management system.

Other related repositories and documents:

 * [Schematic and PCB layout](https://github.com/urbangregorc/vesna-hardware/tree/SNA-LGTC/SNA-LGTC/v1.1.0) for the SNA-LGTC board.
 * [Patched OpenOCD](https://github.com/avian2/openocd/tree/sna-lgtc) for programming the guest VESNA SNC board.
 * [Instructions](https://github.com/avian2/vesna-drivers/blob/logatec-3/README.beaglebone.md)
   for compiling, uploading and debugging firmware for the guest VESNA SNC
   board using *vesna-drivers* from the host SNA-LGTC board.
 * [NodeSpectrumSensorLocal](https://github.com/avian2/vesna-drivers/tree/logatec-3/Applications/Logatec/NodeSpectrumSensorLocal), application for controlling the SNE-ISMTV radio on the guest board using ALH protocol over the UART.
 * [VESNA management system](https://github.com/matevzv/vesna-management-system), web application for remote access over ALH to the guest VESNA SNC.
 * [Boot scripts](https://github.com/avian2/bone-boot-scripts/tree/sna-lgtc), customized BeagleBone boot scripts for SNA-LGTC.
