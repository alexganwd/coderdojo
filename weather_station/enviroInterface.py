from bme280 import BME280

try:
    from smbus2 import SMBus
except ImportError:
    raise ("Error importing smbus2, Controller not supported")

class enviroInterface(object):  
    ''' Access enviro+ interface '''  
    def __init__(self):
        self.bus = SMBus(1)
        self.bme280 = BME280(i2c_dev=bus)

    def get_temperature(self):
        ''' Temperature collected on Celsius '''
        return self.bme280.get_temperature()

    def get_pressure(self):
        ''' Pressure collected on hPa '''
        return self.bme280.get_pressure()

    def get_humedity(self):
        ''' Pressure collected on % '''
        return self.bme280.get_humedity()