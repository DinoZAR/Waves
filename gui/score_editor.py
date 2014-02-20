'''
Created on Feb 20, 2014

@author: spencer
'''
from PySide.QtGui import QWidget

from forms.score_editor_ui import Ui_ScoreEditor
class ScoreEditor(QWidget):
    '''
    The editor used to edit my scores.
    '''

    def __init__(self, parent=None):
        super(ScoreEditor, self).__init__(parent)
        
        self.ui = Ui_ScoreEditor()
        self.ui.setupUi(self)