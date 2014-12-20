import smbus

class GenericSensor():
    name = "Unknown"
    def __init__(self):
        pass
    def fields(self):
        pass
    def values(self):
        pass

class I2CSensor(GenericSensor):
    bus = None

    def connect(self):
        if I2CSensor.bus == None:
            I2CSensor.bus = smbus.SMBus(1)
    
    def disconnect(self):
        pass