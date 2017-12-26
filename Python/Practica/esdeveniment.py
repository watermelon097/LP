#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 16:03:14 2017

@author: alcasser
"""

class Esdeveniment:
    'classe per a tractar esdeveniments'
    totalEdmts = 0
    
    def __init__(self, nom, nom_lloc, carrer, barri, districte, \
                 classificacions, data_i, data_f, geo_pos, transport = None):
        self.nom = nom
        self.nom_lloc = nom_lloc
        self.carrer = carrer
        self.barri = barri
        self.districte = districte
        self.data_i = data_i
        self.data_f = data_f
        self.classificacions = classificacions
        self.geo_pos = geo_pos
        self.__build_info()
        self.transport = transport
        Esdeveniment.totalEdmts += 1
    
    def __build_info(self):
        self.info = self.nom + self.nom_lloc + self.carrer + self.barri + \
                    self.classificacions + self.districte
    def get_info(self):
        return self.info
        
    def get_dates(self):
        return (self.data_i, self.data_f)
    
    def get_pos(self):
        return self.geo_pos
    
    def set_transport(self, transport):
        self.transport = transport
    
    def get_transport(self):
        return self.transport         