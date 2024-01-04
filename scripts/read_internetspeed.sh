#!/bin/bash
. /home/pi/.bashrc
python3 /home/pi/broadband-speed-test/scripts/speedtest_influxdb2.py &>> /home/pi/log/speedtest_influxdb2.log