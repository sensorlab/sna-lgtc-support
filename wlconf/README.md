# WL1837 module firmware configuration

This is the configuration file for the wl1837 module.

It was created using the `configure-device.sh` script from TI (it can be found
on the BeagleBone Wireless Green image at `/usr/share/ti/wlconf`).

This configuration enables 5 GHz support on the radio.

`wl18xx-conf.bin` file should be placed into `/lib/firmware/ti-connectivity`.

Also note: if the `wlan0` interface says "Cannot assign requested address" or
something similar, this is due to an invalid MAC being set. Remove
`/lib/firmware/ti-connectivity/wl1271-nvs.bin`.

Further reading:

 * [WL18xx Writing MAC address](http://processors.wiki.ti.com/index.php/WL18xx_Writing_MAC_address)
 * [WiLink Troubleshooting](http://processors.wiki.ti.com/index.php/WiLink_Troubleshooting)
