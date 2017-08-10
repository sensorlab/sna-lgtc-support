# Device Tree Source

## Building

The `dtb` that was built using these steps was tested on the `4.4.30-ti-r64` kernel
that ships with the `bone-debian-8.6-seeed-iot-armhf-2016-11-06-4gb.img` image.

Requirements:

 * BeagleBoard Linux source (https://github.com/avian2/linux, branch sna-lgtc)

Prepare the kernel tree (run on the top of the kernel source):

    $ make ARCH=arm CROSS_COMPILE=arm-none-eabi- scripts

The build the `dtb` here with:

    $ make KERNEL=~/src/linux

Where `KERNEL` should point to the top of the kernel tree.

## Installation

Copy the appropriate `dtb` file into `/boot/dtbs/4.4.30-ti-r64/`. The
`/boot/uEnv.txt` file should contain the name of the `dtb` file to use. For
example:

    dtb=am335x-lgtc-wireless.dtb
