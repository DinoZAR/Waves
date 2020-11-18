"""
Created on Feb 20, 2014

@author: Spencer Graffe
"""
from part import Part


class Score(object):
    """
    This stores the musical content of the score.
    """

    def __init__(self):
        """
        Constructor
        """
        self.title = "Untitled"
        self.author = "Unauthored"

        self.parts = []

        # Add a default part
        self.parts.append(Part())

        # These events are global in scope
        self.globalEvents = []

    def dump(self):
        """
        Prints out a report to view the contents inside of the score.
        """
        out = "Title: " + self.title + "\n"
        out += "Author: " + self.author + "\n"
        out += "---------------------------------------------------\n"
        for p in self.parts:
            out += p.dump() + "\n"
        out += "---------------------------------------------------"
        return out
