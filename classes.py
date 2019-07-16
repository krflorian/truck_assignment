# -*- coding: utf-8 -*-
"""
Created on Wed May 29 15:11:56 2019

@author: kr_fl
"""

import numpy as np

def euclidean_distance(x_1, y_1, x_2, y_2):
    dist = np.sqrt((x_2-x_1)**2 + (y_2-y_1)**2)
    return dist

class truck():
    def __init__(self, name):
        self.driver_name = name
        self.plate_number = ''
        self.telephone_number = ''
        self.nationality = 'German'
        self.position = (0,0)
        self.cost_empty = 0.5
        self.cost_full = 1
        self.driving_time = 10
    def __str__(self):
        return self.driver_name + ' is currently at ' + str(self.position)        
    def set_position(self, lat, lon):
        self.position = (lat, lon)
    def set_driving_time(self, time):
        self.driving_time = time
    def distance_to(self, load):
        dist = euclidean_distance(self.position[0], self.position[1],
                                  load.position_load[0], load.position_load[1])
        return dist
        
class load():
    def __init__(self, id):
        self.load_number = id
        self.position_load = (0,0)
        self.position_unload = (0,0)
        self.revenue = 1000
        self.distance = 0
    def __str__(self):
        return self.load_number + ' from ' + str(self.position_load) + ' to ' + str(self.position_unload)       
    def set_position_load(self, lat, lon):
        self.position_load = (lat, lon)
        # maybe add update distance??? 
    def set_position_unload(self, lat, lon):
        self.position_unload = (lat, lon)
        # maybe add update distance??? 
    def distance_to(self, truck):
        dist = euclidean_distance(self.position[0], self.position[1],
                                  truck.position[0], truck.position[1])
        return dist   
    def update_distance(self):
        dist = euclidean_distance(self.position_load[0], self.position_load[1],
                                  self.position_unload[0], self.position_unload[1])
        self.distance = dist
        return dist   

