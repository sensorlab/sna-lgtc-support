# Munin plugins for SNA-LGTC

This directory contains some useful custom Munin plugins for monitoring the
health of SNA-LGTC nodes.

## Wireless network monitoring

This plugin reports management network signal strength, bit rate, link quality
and transmit power.

Copy the `iw_` file to `/etc/munin/plugins/iw_wlan0` (where `wlan0` is the
wireless interface on the SNA-LGTC node that is used for the management network
connection).
