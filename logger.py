import threading
import time
import csv
from datetime import datetime

from sensors.MC9808 import MC9808
from sensors.Dummy import DummySensor

class Logger(threading.Thread):
    sensor_list = []
    cycle = 1
    
    def __init__(self, filename):
        threading.Thread.__init__(self)
        self.kill_me = False
        self.filename = filename
        
    def add_sensor(self, sensor):
        self.sensor_list.append(sensor)
    
    def get_time(self):
        return datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    
    def run(self):
        self.kill_me = False
        
        # Initialize the sensor
        for sens in self.sensor_list:
            print("Connecting sensor {0}...".format(sens.name))
            sens.connect()
   
        # Open the file
        self.file = open(self.filename, 'a')
        
        # Intialize the logger
        self.csv = csv.writer(self.file, delimiter=';', quotechar='"')
        
        # Run until stop is called
        while not self.kill_me:
            values = []
            # Collect the values
            for sens in self.sensor_list:
                values += sens.values()
            # Convert to string and replace the points    
            str_values = ["{0}".format(v).replace('.', ',') for v in values]
            # Insert the timestamp
            str_values.insert(0, self.get_time())
            print(str_values)
            # Write the values to the file
            self.csv.writerow(str_values)
            time.sleep(self.cycle)
        else:
            print("\nStopping...")
            for sens in self.sensor_list:
                print("Disconnecting sensor {0}...".format(sens.name))
                sens.disconnect()
            print("Closing file...")
            self.file.close()

    def stop(self):
        self.kill_me = True

if __name__ == '__main__':
    logger = Logger('output/log.csv')
    
    logger.add_sensor(MC9808())
    
    logger.start()

    while logger.isAlive():
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            logger.stop()
            break