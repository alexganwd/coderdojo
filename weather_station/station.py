from connectionDB import influxdbManager
import connectionDB
import time
from enviroInterface import enviroInterface

# from enviroInterface import enviroInterface
DATASOURCE = "mStation"

#  Setting up the connection to Influx to push metrics
influx_connection =  influxdbManager(DATASOURCE)

while True:
# Collect bme280 sensor data ( Temperature, Pressure, Humedity)
# temperature = enviroInterface.get_temperature()
    json_pack = format_bme280(temperature=enviroInterface.get_temperature(), 
    pressure=enviroInterface.get_pressure(), 
    humedity=enviroInterface.get_humedity()
    )
    influx_connection.write_points(json_pack)
    time.sleep(30)