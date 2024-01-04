#!/bin/bash
. /home/pi/.bashrc
echo $INFLUXDB_TOKEN >> /home/pi/log/speedtest_influxdb2.log
 /usr/bin/python /home/pi/broadband-speed-test/scripts/speedtest_influxdb2.py &>> /home/pi/log/speedtest_influxdb2.log