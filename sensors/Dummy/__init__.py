import sensors

class DummySensor(sensors.I2CSensor):
    name = "Dummy"
    def fields(self):
        return ['Value A', 'Value B']
    def values(self):
        return [1.23, 4.56]