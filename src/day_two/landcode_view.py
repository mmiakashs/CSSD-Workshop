#!/usr/bin/env python

import pandas as pd
import numpy as np
import matplotlib as mlt
import matplotlib.pyplot as plt
import math
import sys

WIDTH = 43200
HEIGHT = 21600

def geo_point_to_pixel(lat,lon):
    lat_ratio = (lat-90)/180
    lon_ratio = (lon+180)/360
    pixel_x = math.floor(-(HEIGHT-1)*lat_ratio)
    pixel_y = math.floor((WIDTH-1)*lon_ratio)
    return (pixel_x, pixel_y)

def get_place_type(place_type):
    if (place_type == 0):
        return 'Water'
    else:
        return 'Land'

def deg_to_pixel(viewpoint_len,total_deg):
    deg_to_pixel_len = viewpoint_len*(WIDTH)/total_deg
    return deg_to_pixel_len


data = np.memmap("../../data/gl-latlong-1km-landcover.bsq", shape=(HEIGHT,WIDTH))

while(True):
    input = sys.stdin.readline().split()
    user_in_lat = float(input[0])
    user_in_lon = float(input[1])

    pixel_x,pixel_y = geo_point_to_pixel(user_in_lat,user_in_lon)
    deg_to_pixel_len_x = int(deg_to_pixel(10,360))
    deg_to_pixel_len_y = int(deg_to_pixel(10,180))

    plt.imshow(data[pixel_x:pixel_x+deg_to_pixel_len_x , pixel_y:pixel_y+deg_to_pixel_len_y])
    plt.show()