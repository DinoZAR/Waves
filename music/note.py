'''
Created on Feb 23, 2014

@author: Spencer Graffe
'''
from music.event import Event

class Note(Event):
    '''
    Represents a note that emits a constant pitch for a certain length of time
    '''

    def __init__(self, timeStamp, duration, pitch):
        super(Note, self).__init__(timeStamp, duration)
        
        self.pitch = pitch
        