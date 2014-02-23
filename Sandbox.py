'''
Created on Feb 23, 2014

A place to test out and play with some ideas.

@author: Spencer Graffe
'''
from music.score import Score

if __name__ == '__main__':
    
    myScore = Score()
    
    print 'My score:'
    print myScore.dump()
    
    print 'Done!'