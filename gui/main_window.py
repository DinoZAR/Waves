import os
from PySide.QtGui import QMainWindow
from forms.main_window_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    '''
    Lots of neat things about this.
    '''

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)