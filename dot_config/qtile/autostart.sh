#!/bin/sh

# systray battery icon
# cbatticon -u 5 &
# systray volume
# volumeicon &
# systray bluetooth
blueman-applet &

# keyboard config
setxkbmap es &

# wallpaper
nitrogen --restore &

# nextcloud
nextcloud &
