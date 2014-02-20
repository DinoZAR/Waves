'''
Miscellaneous functions that don't have a specific place, but are generally
useful.

@author: Spencer Graffe
'''
import sys
import os

_APPNAME = "Waves"

def app_data(resource):
    '''
    Returns a pathname inside of the user's app data directory using resource
    as the relative path inside of it.
    '''
    if sys.platform == 'darwin':
        from AppKit import NSSearchPathForDirectoriesInDomains
        # http://developer.apple.com/DOCUMENTATION/Cocoa/Reference/Foundation/Miscellaneous/Foundation_Functions/Reference/reference.html#//apple_ref/c/func/NSSearchPathForDirectoriesInDomains
        # NSApplicationSupportDirectory = 14
        # NSUserDomainMask = 1
        # True for expanding the tilde into a fully qualified path
        appdata = os.path.join(NSSearchPathForDirectoriesInDomains(14, 1, True)[0], _APPNAME)
    elif sys.platform == 'win32':
        appdata = os.path.join(os.environ['APPDATA'], _APPNAME)
    else:
        appdata = os.path.expanduser(os.path.join("~", "." + _APPNAME))
    
    return os.path.join(appdata, resource)