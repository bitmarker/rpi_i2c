import sensors

class MC9808(sensors.I2CSensor):
    name = "MC9808"
    def fields(self):
        return ['Temp.', 'Pressure']
    def values(self):
        return [22.34, 0.00]