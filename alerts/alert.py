# -*- coding: utf-8 -*-
'''
Created on 14/06/2013
@author: Marcos Aguayo <marcos@aguayo.es>
'''
import gui as g



class Alert():
    '''
    Class to handle alerts
    '''
    
    def __init__(self, *args, **kwargs):
        print "Llamado"
        
    def set_orden(self, orden):
        self.orden = orden
        print self.orden