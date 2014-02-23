'''
Created on Feb 23, 2014

@author: Spencer Graffe
'''

class Part(object):
    '''
    Class used to store and manipulate data about a part.
    '''

    def __init__(self):
        
        self.label = 'Part'
        
        # TODO: Figure out a settings object to put in a Part
        self.settings = None        
        
        # These events are specific to this part
        self.events = []