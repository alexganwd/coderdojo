from influxdb import InfluxDBClient

class influxdbManager:
    ''' Class to manage access to InfluxDB '''

    def __init__(self,database):
        self.client = InfluxDBClient(database=database)
        self.client.create_database(database)
    
    def write_points(self, json_body):
        self.client.write_points(json_body)
