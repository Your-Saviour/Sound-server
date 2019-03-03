MAC_ADDRESS=$(ifconfig | grep wlx | grep -oE "[0-9a-f:]{17}")
IFACE_NAME=$(ifconfig | grep -oE "wlx[^ ]+")

nmcli c modify PGSStudent 802-11-wireless.mac-address $MAC_ADDRESS
nmcli c modify PGSStudent connection.interface-name $IFACE_NAME
