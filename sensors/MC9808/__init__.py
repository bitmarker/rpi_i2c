import sensors

class MC9808(sensors.I2CSensor):
    name = "MC9808"
    
    def fields(self):
        return ['Temp.']
    
    def values(self):
        temp_raw = self.bus.read_i2c_block_data(0x18, 0x05, 2)
        temp_ub = temp_raw[0]
        temp_lb = temp_raw[1]
        
        temp_ub = temp_ub & 0x1F

        if (temp_ub & 0x10) == 0x10:
            temp_ub = temp_ub & 0x0F
            temperature = -1*(256 - (temp_ub * 16.0 +  temp_lb / 16.0))
        else:
            temperature = (temp_ub * 16.0 + temp_lb / 16.0)
        
        return [temperature]