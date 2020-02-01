dry_run = False
if dry_run:
    import mock_bme280
else:
    from smbus2 import SMBus
    from bme280 import BME280

import time
import sqlite3

try:
    if dry_run:
        db_connection = sqlite3.connect('meassurements-tests')
    else:
        db_connection = sqlite3.connect('meassurements')

except sqlite3.Error as e:
    print("Database error: %s" %e)

except Exception as e:
    print("Exception in _query: %s" %e)
    
print(sqlite3.version)
db_connection.execute('CREATE TABLE IF NOT EXISTS bme280 (id Integer primary key AUTOINCREMENT, temperature REAL, humidity REAL, pressure REAL);')
while True:
    #define data
    temperature = mock_bme280.get_temperature()
    pressure = mock_bme280.get_pressure()
    humidity = mock_bme280.get_humidity()

    print ("Temperature " + str(temperature))
    try:
        db_connection.execute('INSERT INTO bme280 (temperature, humidity, pressure) VALUES (?, ?, ?)',  (temperature, humidity, pressure))
        db_connection.commit()
    except sqlite3.IntegrityError as e:
        print("Exception in _query %s" % e) 

    print ("Humedity: " + str(humidity))
    print ("Pressure: " + str(pressure))
    time.sleep(5)
