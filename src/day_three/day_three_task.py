#!/usr/bin/env python
# coding: utf-8

import pandas as pd


class Parcel(object):
    def __init__(self, parcel_destination, parcel_weight):
        self.weight = parcel_weight
        self.destination = parcel_destination

class Train(object):
    def __init__(self, train_destination, train_capacity, train_no):
        self._destination = train_destination
        self._capacity = train_capacity
        self._train_no = train_no
        self._parcels = []
        self._actual_load = 0
    
    def get_total_number_of_parcels(self):
        return len(self._parcels)
    
    def load_parcel(self,parcel):
        self._actual_load += parcel.weight
        self._parcels.append(parcel)
        
    def can_load_parcel(self,parcel):
        return ((self._actual_load + parcel.weight) < self._capacity) and self.is_destination_match(parcel)

    def is_destination_match(self, parcel):
        return self._destination == parcel.destination
    
    def __str__(self):
        train_description = "Train: {}\nDestination: {}\nCapacity: {:.2f}\nActual Load: {:.2f}\nNumber of parcels: {}\nParcels:\n"\
            .format(self._train_no,
                    self._destination,
                    self._capacity,
                    self._actual_load,
                    self.get_total_number_of_parcels())
        
        parcels_infos = []
        for parcel_info in self._parcels:
            parcels_infos.append("{} {:.2f}".format(parcel_info.destination, parcel_info.weight))

        parcels_infos_concat =  '\n'.join(parcels_infos)

        return train_description + parcels_infos_concat


class Station:
    def __init__(self, parcels_file_name, trains_file_name):
        self.trains_file_name = trains_file_name
        self.parcels_file_name = parcels_file_name
        self.train_no = 1
        self.trains = None
        self.parcels = None
        self.parcels_delivery_status = {}
        self.load_trains_info()
        self.load_parcels_info()

    def load_trains_info(self):

        self.trains = pd.read_csv(self.trains_file_name,
                             sep=' ', comment='#', header=None, index_col=False,
                             names=['train_destination', 'train_max_weight'])

    def load_parcels_info(self):
        parcels_df = pd.read_csv(self.parcels_file_name,
                              sep=' ', comment='#', header=None, index_col=False,
                              names=['parcel_destination', 'parcel_weight'])
        self.parcels = parcels_df.values.tolist()
        self.parcels.reverse()
    
    def load_trains(self):
        for index, train_info in self.trains.iterrows():
            train = Train(train_info['train_destination'],
                          1000.0*train_info['train_max_weight'],
                          self.train_no)
            print('Loading train', self.train_no)
            self.load_parcels(train)
            with open('../../data/train_task/output/train_{}'.format(self.train_no), "w+") as file:
                file.write(str(train))
            self.train_no += 1
                
    def load_parcels(self,train):
        parcels_iterator = len(self.parcels) -1
        while True:
            if (parcels_iterator <=0):
                break
            parcel = Parcel(self.parcels[parcels_iterator][0], self.parcels[parcels_iterator][1])

            if(train.can_load_parcel(parcel) and parcels_iterator not in self.parcels_delivery_status):
                train.load_parcel(parcel)
                self.parcels_delivery_status[parcels_iterator]=True

            parcels_iterator -= 1

station = Station('../../data/train_task/parcels.txt', '../../data/train_task/trains.txt')
station.load_trains()

