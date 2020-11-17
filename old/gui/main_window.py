import os

from PySide.QtGui import QMainWindow

from forms.main_window_ui import Ui_MainWindow
from gui.score_editor import ScoreEditor
from music.score import Score

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
        
        self.addNewScore()
        
        self.connect_signals()
    
    def connect_signals(self):
        
        # MAIN MENU
        self.ui.actionNew.triggered.connect(self.addNewScore)
        self.ui.actionClose_Current_Score.triggered.connect(self.removeCurrentScore)
        
        self.ui.tabWidget.tabCloseRequested.connect(self.removeScore)
        
    def addNewScore(self):
        '''
        Adds a new score.
        '''
        self.addScore(Score())
        
    def addScore(self, score):
        '''
        Creates an editor for the score and adds it as a new tab.
        '''
        editor = ScoreEditor(score)
        self.ui.tabWidget.addTab(editor, editor.getTabLabel())
        
    def removeScore(self, index):
        '''
        Removes a score at the specified index.
        '''
        # TODO: Ask user if they want to save if anything changed
        self.ui.tabWidget.removeTab(index)
        
    def removeCurrentScore(self):
        '''
        Removes the current score in view.
        '''
        if self.ui.tabWidget.count() > 0:
            self.removeScore(self.ui.tabWidget.currentIndex())