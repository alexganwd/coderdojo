import json

def format_bme280(temperature, pressure, humedity)
json_body = [{
            "measurement": "temperature",
            "tags": {
                "host": "server01",
                "region": "us-west"
            },
            "time": "2019-11-19T23:00:00Z",
            "fields": {
                "temp": 3            }
        }]
influx_connection.write_points(json_body)