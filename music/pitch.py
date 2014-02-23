'''
Created on Feb 23, 2014

@author: Spencer Graffe
'''

SEMITONE_MAP = {'a' : 0,
                'a#/bb' : 1,
                'b' : 2,
                'c' : 3,
                'c#/db' : 4,
                'd' : 5,
                'd#/eb' : 6,
                'e' : 7,
                'f' : 8,
                'f#/gb' : 9,
                'g' : 10,
                'g#/ab' : 11}

class Pitch(object):
    '''
    This object is used to represent a pitch in music.
    '''
    
    # Defaults are set to middle C
    DEFAULT_SEMITONE = SEMITONE_MAP['c']
    DEFAULT_OCTAVE = 4

    def __init__(self):
        self.semitone = Pitch.DEFAULT_SEMITONE
        self.octave = Pitch.DEFAULT_OCTAVE
        
        # This value is bound between -100 to 100, a percentage of a semitone
        # that it is bent to
        self.bend = 0