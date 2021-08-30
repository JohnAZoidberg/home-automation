#!/bin/sh
 
# Read Temperature
tempread=`cat /sys/bus/w1/devices/28-031297799fa7//w1_slave`
# Format
temp=`echo "scale=2; "\`echo ${tempread##*=}\`" / 1000" | bc`
 
# Output
echo "The measured temperature is " $temp "°C"
