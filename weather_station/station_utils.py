from datetime import datetime

def get_current_time():
    return(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'))

def format_bme280(temperature, pressure, humidity, current_time):
    json_body_list = [
        {
            "measurement": "temperature",
            "tags": {
                "sensor": "bme280",
                "type": "temperature"
            },
            "time": current_time,
            "fields": {
                "temperature": temperature            
            }
        },
        {
            "measurement": "pressure",
            "tags": {
                "sensor": "bme280",
                "type": "pressure"
            },
            "time": current_time,
            "fields": {
                "pressure": pressure            }
        },
        {
            "measurement": "humidity",
            "tags": {
                "sensor": "bme280",
                "type": "humidity"
            },
            "time": current_time,
            "fields": {
                "humidity": humidity            
            }
        }
        ]
    return json_body_list