import sys
import os

from PySide.QtGui import QApplication

from gui.main_window import MainWindow

if __name__ == '__main__':
    print 'Starting Waves!'

    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    app.exec_()

    print 'Done!'