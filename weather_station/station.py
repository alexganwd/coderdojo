from connectionDB import influxdbManager
import time
from enviroInterface import enviroInterface
from station_utils import format_bme280, get_current_time

DATASOURCE = "mStation"

#  Setting up the connection to Influx to push metrics
influx_connection =  influxdbManager(DATASOURCE)

# Initialize enviro interface
enviroInterface = enviroInterface()

while True:
# Collect bme280 sensor data ( Temperature, Pressure, Humidity)
    current_time = get_current_time()
    json_pack = format_bme280(temperature=enviroInterface.get_temperature(), 
    pressure=enviroInterface.get_pressure(), 
    humedity=enviroInterface.get_humidity(), current_time=current_time
    )
    influx_connection.write_points(json_pack)
    time.sleep(30)
