import sys
import os

from PySide.QtGui import QApplication

from gui.main_window import MainWindow

if __name__ == '__main__':
    print 'Starting Ocean Composer!'

    app = QApplication(sys.argv)

    with open(os.path.abspath('forms/style.css'), 'rb') as f:
        app.setStyleSheet(unicode(f.read()))
    
    window = MainWindow()
    window.show()
    app.exec_()

    print 'Done!'