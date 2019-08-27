from datetime import datetime

def get_current_time():
    return(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'))

def format_bme280(temperature, pressure, humedity, current_time):
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
            "measurement": "humedity",
            "tags": {
                "sensor": "bme280",
                "type": "humedity"
            },
            "time": current_time,
            "fields": {
                "humedity": humedity            
            }
        }
        ]
    return json_body_list