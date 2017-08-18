# WL1837 Bluetooth support

Currently, Bluetooth isn't configured on boot. To attach it, run:

    $ sudo hciattach /dev/ttyS1 texas 300000

Wi-fi must be enabled for this to work. Note that BeagleBone Green Wireless
scripts expect the Bluetooth HCI to be connected to UART3, but we have it
connected to UART1.

After it has been attached, Bluetooth can be controlled using the
`bluetoothctl` tool:

    $ sudo bluetoothctl
    [NEW] Controller 50:8C:B1:5C:AB:89 sna-lgtc [default]
    [bluetooth]# power on
    Changing power on succeeded
    [bluetooth]#

Bluetooth audio interface is not connected in the hardware and hence cannot be
used.
