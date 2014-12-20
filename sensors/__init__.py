class GenericSensor():
    name = "Unknown"
    def __init__(self):
        pass
    def fields(self):
        pass
    def values(self):
        pass

class I2CSensor(GenericSensor):
    def connect(self):
        pass
    def disconnect(self):
        pass