#!/bin/bash

echo "WMBR Transmitter Sensor Logger starting up..."
echo
echo "Setting system time"
# Our server has no internal clock, so we set it at startup 
rm /etc/localtime
ln -s /usr/share/zoneinfo/America/New_York /etc/localtime
ntpdate pool.ntp.org

echo
echo "Starting logger"
python ~/transmittr/main.py &

echo
echo "Starting web server"
# Make sure the bonescript service isn't trying to hog port 80
systemctl disable bonescript.socket
systemctl disable bonescript.service
systemctl disable bonescript-autorun.service
systemctl stop bonescript.socket
systemctl stop bonescript.service
systemctl stop bonescript-autorun.service

echo
echo "No server available yet..."
