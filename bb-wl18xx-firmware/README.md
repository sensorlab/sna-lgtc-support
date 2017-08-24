# WL1837 module firmware and related scripts

This Debian package is based on the `bb-wl18xx-firmware` package that ships
with BeagleBone SD card images.

The package contains firmware for the WL1837 that has been customized for the
specific module used on the SNA-LGTC boards. It also contains scripts that
set-up Bluetooth functionality on boot.

The source here is a modified copy of [the
repository](https://github.com/rcn-ee/repos/tree/master/bb-wl18xx-firmware/suite/jessie/debian)
by Robert C. Nelson. It is based on commit `e26517c` from that repository.

## WL1837 configuration

The configuration for the WL1837 module is in the `wl18xx-conf.bin` file that
is installed into `/lib/firmware/ti-connectivity`.

The file here was created using the `configure-device.sh` script from TI (it
can be found on the BeagleBone Wireless Green image at `/usr/share/ti/wlconf`).

The current configuration enables 5 GHz support on the radio and sets it up for
two mounted antennas.

Further reading:

 * [WL18xx Writing MAC address](http://processors.wiki.ti.com/index.php/WL18xx_Writing_MAC_address)
 * [WiLink Troubleshooting](http://processors.wiki.ti.com/index.php/WiLink_Troubleshooting)

Note: if the `wlan0` interface cannot be enabled due to `Cannot assign
requested address` or a similar error, this is due to an invalid MAC being set.
Remove `/lib/firmware/ti-connectivity/wl1271-nvs.bin` if it exists.

## Bluetooth

Wi-fi must be enabled for Bluetooth to work. Bluetooth controller is
automatically attached on boot.

Bluetooth can be controlled using the `bluetoothctl` tool:

    $ sudo bluetoothctl
    [NEW] Controller 50:8C:B1:5C:AB:89 sna-lgtc [default]
    [bluetooth]# power on
    Changing power on succeeded
    [bluetooth]#

Bluetooth audio interface is not connected in the hardware and hence cannot be
used.

Note that on BeagleBone Green Wireless, Bluetooth HCI pins are connected
slightly differently than on SNA-LGTC. BBGW uses UART3 for Bluetooth, but
SNA-LGTC uses UART1. BBGW uses GPIO1_28 for BL_EN pin, SNA-LGTC uses GPIO3_18.
