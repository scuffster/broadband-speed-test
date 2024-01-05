#!/bin/bash
. /home/pi/.bashrc
echo speed read run at $(date)
# environment
export INFLUXDB_TOKEN=tOuF47u-V_9hqBkZaX8bb5UJftvtfPNwHTeZXS297jDeMgMGy8-oG61GjIZL_p2ynU813omhCrSZduOFzH4HoA==
/usr/bin/python  /home/pi/broadband-speed-test/scripts/speedtest_influxdb2.py &>> /home/pi/log/read_internetspeed.log