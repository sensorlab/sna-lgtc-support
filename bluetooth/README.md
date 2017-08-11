## Bluetooth support

Currently, Bluetooth isn't configured on boot. To attach it, run:

    hciattach /dev/ttyS1 texas 300000

Wi-fi must be enabled for this to work. Note that BeagleBone Green Wireless
scripts expect the Bluetooth HCI to be connected to UART3, but we have it
connected to UART1.
