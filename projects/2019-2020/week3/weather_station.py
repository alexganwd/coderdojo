import mock_bme280
import time

while True:

    # define data
    temperature = mock_bme280.get_temperature()
    pressure = mock_bme280.get_pressure()
    humedity = mock_bme280.get_humidity()

    print ("Temperature " + str(temperature))
    print ("Humedity: " + str(humedity))
    print ("Pressure: " + str(pressure))
    time.sleep(5)
