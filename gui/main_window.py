import os
from PySide.QtGui import QMainWindow
from forms.main_window_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    '''
    The main window that hosts the application.
    '''

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)