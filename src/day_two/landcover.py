#!/usr/bin/env python

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


data = np.memmap("../../data/gl-latlong-1km-landcover.bsq", shape=(HEIGHT,WIDTH))

plt.imshow(data[::50,::50])

print("Give your Coordinates")

# args = sys.argv
# user_in_lat = float(args[1])
# user_in_lon = float(args[2])


while(True):
    input = sys.stdin.readline().split()
    user_in_lat = float(input[0])
    user_in_lon = float(input[1])

    place_type = data[geo_point_to_pixel(user_in_lat,user_in_lon)]
    print("({},{}) is {}".format(user_in_lat, user_in_lon, get_place_type(place_type)))