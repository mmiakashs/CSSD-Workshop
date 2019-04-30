#!/usr/bin/env python

import pandas as pd
import numpy as np
import matplotlib as mlt
import matplotlib.pyplot as plt
import math


WIDTH = 43200
HEIGHT = 21600
data = np.memmap("../../data/gl-latlong-1km-landcover.bsq", shape=(HEIGHT,WIDTH))
data.shape

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

colnames=['DATE TIME','LAT', 'LON', 'PROF','MAGNITUDE', 'FONTE'] 
df = pd.read_csv('../../data/events_4.5.txt', skiprows=7, delimiter=';', names=colnames,index_col=False)
df.head()

place_types = []
for index, row in df.iterrows():
    place_type = data[geo_point_to_pixel(row['LAT'],row['LON'])]
    place_types.append(get_place_type(place_type))

df['PLACE_TYPE'] = pd.Series(place_types)
df.head()

df.to_csv('../../data/modified_earthquake_events.csv',sep=';',index=False)