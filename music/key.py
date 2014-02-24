'''
Created on Feb 24, 2014

@author: Spencer Graffe
'''
from event import Event
from pitch import Pitch

class KeyEvent(Event):
    '''
    Represents a key change that occurs instantaneously at the point of
    insertion.
    '''

    def __init__(self, timeStamp, key):
        super(KeyEvent, self).__init__(timeStamp)
        self.key = key

class Key(object):
    '''
    Class used for calculating the accidentals required for each note.
    '''
    
    # Output flags telling caller which accidental to add to the note
    NOTHING = 0
    SHARP = 1
    FLAT = 2
    NATURAL = 3
    
    def __init__(self):
        '''
        Setting the internal data is done by calling functions after
        construction, such as major(), harmMinor(), etc.
        '''
        # Maps a semitone to the accidental required for that semitone
        self._semiMap = {}
        
        # Creates a default major key
        self.major(Pitch())
    
    def major(self, pitch):
        '''
        Creates a key in the major scale. The pitch represents the tonic of the
        key.
        '''
        
        # Lit of semitone accidentals relative to the first semitone (there must
        # always be 12)
        mySemiList = [self.NOTHING,
                      self.SHARP,
                      self.NOTHING,
                      self.SHARP,
                      self.NOTHING,
                      self.NOTHING,
                      self.SHARP,
                      self.NOTHING,
                      self.SHARP,
                      self.NOTHING,
                      self.SHARP]
    
    def harmonicMinor(self, pitch):
        '''
        Creates a key in the harmonic minor scale. The pitch represents the
        tonic of the key.
        '''
        pass
    
    def naturalMinor(self, pitch):
        '''
        Creates a key in the natural minor scale. The pitch represents the tonic
        of the key.
        '''
        pass