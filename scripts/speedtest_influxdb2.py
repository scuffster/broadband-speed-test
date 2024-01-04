#from influxdb import InfluxDBClient
import influxdb_client, os, time, re
import subprocess
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import datetime

token = os.environ.get("INFLUXDB_TOKEN")
org = "speedtest"
url = "http://speedy01.local:8086"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

response = subprocess.Popen('/usr/bin/speedtest --accept-license --accept-gdpr', shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')

ping = re.search('Latency:\s+(.*?)\s', response, re.MULTILINE)
download = re.search('Download:\s+(.*?)\s', response, re.MULTILINE)
upload = re.search('Upload:\s+(.*?)\s', response, re.MULTILINE)
jitter = re.search('Latency:.*?jitter:\s+(.*?)ms', response, re.MULTILINE)

ping = ping.group(1)
download = download.group(1)
upload = upload.group(1)
jitter = jitter.group(1)

bucket = "speedtest"

write_api = client.write_api(write_options=SYNCHRONOUS)

#for value in range(5):
#    point = (
#        Point("measurement1")
#        .tag("tagname1", "tagvalue1")
#        .field("field1", value)
#    )
#    write_api.write(bucket=bucket, org="speedtest", record=point)
#    time.sleep(1)  # separate points by 1 second

speed_data = [
    {
        "measurement" : "internet_speed",
        "tags" : {
            "host": "speedy01"
        },
        "fields" : {
            "download": float(download),
            "upload": float(upload),
            "ping": float(ping),
            "jitter": float(jitter)
        }
    }
]
write_api.write(bucket=bucket, org="speedtest", record=speed_data)

#client = InfluxDBClient('localhost', 8086, 'speedmonitor', 'pimylifeup', 'internetspeed')


#client.write_points(speed_data)

query_api = client.query_api()

query = """from(bucket: "speedtest")
 |> range(start: -10m)
 |> filter(fn: (r) => r._measurement == "internet_speed")"""
tables = query_api.query(query, org="speedtest")

#for table in tables:
#    for record in table.records:
#        print(record)
print(datetime.datetime.now())
print(speed_data)