import os

from PySide.QtGui import QMainWindow

from forms.main_window_ui import Ui_MainWindow
from gui.score_editor import ScoreEditor

class MainWindow(QMainWindow):
    '''
    The main window that hosts the application.
    '''

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Clear out all of the tabs
        self.ui.tabWidget.clear()
        
    def addScore(self, score):
        '''
        Creates an editor for the score and adds it as a new tab.
        '''
        editor = ScoreEditor()
        