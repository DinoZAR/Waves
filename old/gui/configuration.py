'''
Created on Feb 19, 2014

Used to store the configuration settings for my program. For the configuration
to remain constant, this module must always be imported using the same path.

@author: Spencer Graffe
'''

_CONFIG_DATA = {}

def _getValue(key, defaultValue=None):
    
    if key in _CONFIG_DATA:
        print 'Yes!'
    else:
        if defaultValue is not None:
            print 'Using default value!'
        else:
            raise ValueError('Attempting to get key ' + key + ' that doesn\'t exist without providing default value.')

def _setValue(key, val, defaultValue=None):
    
    if key in _CONFIG_DATA:
        pass
    else:
        pass