'''
Created on Feb 23, 2014

@author: Spencer Graffe
'''
from fractions import Fraction

class Event(object):
    '''
    A musical event that has a time-stamp and duration. By default, an event
    is instantaneous, which means that its duration is 0. Also, both the
    time-stamp and the duration are represented as fractions, which allows for
    a much higher level of accuracy when rendering to output formats such as
    MIDI.
    '''

    def __init__(self, timeStamp, duration=Fraction(0,1)):
        self.timeStamp = timeStamp
        self.duration = duration
        
    def timeAfter(self):
        '''
        Returns the time-stamp after this event.
        '''
        return self.timeStamp + self.duration