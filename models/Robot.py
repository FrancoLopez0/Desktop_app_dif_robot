
from interfaces import IMobileRobot
from dataclasses import dataclass

class Magnetometer():
    def __init__(self):
        self.mx = None
        self.my = None
        self.max_mx = -999999
        self.max_my = -999999
        self.min_mx = 999999
        self.min_my = 999999
        self.bias_x = 0
        self.bias_y = 0
        self.scale_x = 0
        self.scale_y = 0
    
    def calibrate_magnetometer(self):
        self.bias_x =(self.max_mx + self.min_mx)/2
        delta_x = (self.max_mx - self.min_mx)/2

        self.bias_y =(self.max_my + self.min_my)/2
        delta_y = (self.max_my - self.min_my)/2

        delta_avg = (delta_y+delta_x)/2

        self.scale_x = delta_avg / delta_x
        self.scale_y = delta_avg / delta_y

        return [self.scale_x, self.scale_y, self.bias_x, self.bias_y]
    
    def set_params_to_calibrate(self, min_mx, max_mx, min_my, max_my):
        self.max_mx = max_mx
        self.min_mx = min_mx
        
        self.max_my = min_my
        self.min_my = max_my
    
    def get_params_to_calibrate(self):
        return [self.min_mx, self.max_mx, self.min_my, self.max_my]
        
    def get_values_to_calibrate(self, value_x, value_y):
        if value_x > self.max_mx:
            self.max_mx = value_x
        if value_y > self.max_my:
            self.max_my = value_y
        
        if value_x < self.min_mx:
            self.min_mx = value_x
        if value_y < self.min_my:
            self.min_my = value_y

class Robot():
    def __init__(self):
        self.magnetometer = Magnetometer()

    def calibrate_magnetometer(self):
        return self.magnetometer.calibrate_magnetometer()

    def set_values_to_calibrate_magnetometer(self, data):
        # self.magnetometer.get_values_to_calibrate(data[0], data[1])
        self.magnetometer.set_params_to_calibrate(data[0], data[1], data[2], data[3])
