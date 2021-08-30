#!/bin/sh
DATE=$(date)
JOURNAL_ENTRY=$(journalctl -n1 -ru nightlight --output-fields=MESSAGE -o verbose | grep MESSAGE | awk -F= '{ print $2}')
echo "$DATE\n$JOURNAL_ENTRY" | tee /home/pi/display
