# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Spencer\Documents\Projects\Waves\Waves\forms/main_window.ui'
#
# Created: Tue Nov 19 07:24:38 2013
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("/* Application-wide properties*/\n"
"* {\n"
"    color: black;\n"
"    font-size: 12pt;\n"
"}\n"
"\n"
"QMainWindow {\n"
"    background-color: #e0ded8;\n"
"}\n"
"\n"
"QMenuBar {\n"
"    background-color: #e0ded8;\n"
"    margin: 0px;\n"
"    border: 0px;\n"
"}\n"
"\n"
"    QMenuBar::item {\n"
"        spacing: 3px; /* spacing between menu bar items */\n"
"        padding: 7px 12px;\n"
"        background: transparent;\n"
"    }\n"
"\n"
"        QMenuBar::item:selected { /* when selected using mouse or keyboard */\n"
"            background: #efd4a9;\n"
"            border: 1px solid #dcc399;\n"
"        }\n"
"\n"
"        QMenuBar::item:pressed {\n"
"            background: #efd4a9;\n"
"            border: 0px solid #dcc399;\n"
"        }\n"
"\n"
"QMenu {\n"
"    margin: 0px;\n"
"    border: 0px;\n"
"}\n"
"\n"
"    QMenu::item {\n"
"        padding: 12px 24px;\n"
"        background: #efd4a9;\n"
"    }\n"
"\n"
"        QMenu::item:selected {\n"
"            background: #0094ff;\n"
"            color: white;\n"
"        }\n"
"\n"
"    QMenu::separator {\n"
"        height: 1px;\n"
"        background-color: black;\n"
"    }\n"
"\n"
"    QMenu::indicator {\n"
"        width: 13px;\n"
"        height: 13px;\n"
"    }\n"
"\n"
"\n"
"/* Actual controls*/\n"
"\n"
"QLabel {\n"
"}\n"
"\n"
"QPushButton {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"    padding: 10px 20px;\n"
"}\n"
"\n"
"    QPushButton:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: #0094ff;\n"
"    }\n"
"\n"
"\n"
"QSlider {\n"
"    height: 35px;\n"
"}\n"
"\n"
"\n"
"QSlider::groove:horizontal {\n"
" background: #efd4a9;\n"
"border: 1px solid #dcc399;\n"
"height: 20px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
" background: #0094ff;\n"
"height: 15px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
" background: #efd4a9;\n"
"border: 1px solid #dcc399;\n"
"height: 15px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"width: 13px;\n"
"margin-top: -5px;\n"
"margin-bottom: -5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"}\n"
"\n"
"\n"
"\n"
"QRadioButton:hover {\n"
"    background: #535a57;\n"
"}\n"
"\n"
"QRadioButton:pressed {\n"
"    background: #ff7500;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 32px;\n"
"    height: 32px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"    QRadioButton::indicator::unchecked {\n"
"        image: url(forms/icons/check_empty.png);\n"
"    }\n"
"\n"
"    QRadioButton::indicator:unchecked:hover {\n"
"        image: url(forms/icons/check_empty.png);\n"
"    }\n"
"\n"
"    QRadioButton::indicator:unchecked:pressed {\n"
"        image: url(forms/icons/check_empty.png);\n"
"    }\n"
"\n"
"    QRadioButton::indicator::checked {\n"
"        image: url(forms/icons/check_full.png);\n"
"    }\n"
"\n"
"    QRadioButton::indicator:checked:hover {\n"
"        image: url(forms/icons/check_full.png);\n"
"    }\n"
"\n"
"    QRadioButton::indicator:checked:pressed {\n"
"        image: url(forms/icons/check_full.png);\n"
"    }\n"
"\n"
"\n"
"QCheckBox {\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"    QCheckBox:hover {\n"
"        background: #535a57;\n"
"    }\n"
"\n"
"    QCheckBox:pressed {\n"
"        background: #0094ff;\n"
"    }\n"
"\n"
"    QCheckBox::indicator {\n"
"        width: 24px;\n"
"        height: 24px;\n"
"    }\n"
"\n"
"        QCheckBox::indicator::unchecked {\n"
"            image: url(forms/icons/check_empty.png);\n"
"        }\n"
"\n"
"        QCheckBox::indicator:unchecked:hover {\n"
"            image: url(forms/icons/check_empty.png);\n"
"        }\n"
"\n"
"        QCheckBox::indicator:unchecked:pressed {\n"
"            image: url(forms/icons/check_empty.png);\n"
"        }\n"
"\n"
"        QCheckBox::indicator::checked {\n"
"            image: url(forms/icons/check_full.png);\n"
"        }\n"
"\n"
"        QCheckBox::indicator:checked:hover {\n"
"            image: url(forms/icons/check_full.png);\n"
"        }\n"
"\n"
"        QCheckBox::indicator:checked:pressed {\n"
"            image: url(forms/icons/check_full.png);\n"
"        }\n"
"\n"
"\n"
"QTabWidget {\n"
"    background-color: #ff7500;\n"
"}\n"
"\n"
"    QTabWidget::pane {\n"
"        border-top: 3px solid #0094ff;\n"
"    }\n"
"\n"
"QTabBar::tab {\n"
"    background: #efd4a9;\n"
"    border: 1px solid #dcc399;\n"
"    min-width: 8ex;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"    QTabBar::tab:hover {\n"
"        background: #6fc2ff;\n"
"        border: 0px;\n"
"    }\n"
"\n"
"    QTabBar::tab:selected {\n"
"        background: #0094ff;\n"
"        color: white;\n"
"        border: 0px solid #dcc399;\n"
"    }\n"
"\n"
"    QTabBar::tab:!selected {\n"
"        margin-top: 5px;\n"
"    }\n"
"\n"
"QTabBar::close-button {\n"
"    image: url(:/icons/close-tab.png);\n"
"    subcontrol-position: right;\n"
"}\n"
"\n"
"QTabBar::close-button:!selected {\n"
"    margin-top: 5px;\n"
" }\n"
" QTabBar::close-button:hover {\n"
"image: url(:/icons/close-tab-hover.png);\n"
" }\n"
"")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setContentsMargins(7, 7, 7, 7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet("")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/Media-Play-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalSlider = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider.setStyleSheet("")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout.addWidget(self.horizontalSlider)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 36))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtGui.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionManual = QtGui.QAction(MainWindow)
        self.actionManual.setObjectName("actionManual")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionCut = QtGui.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtGui.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtGui.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionUndo = QtGui.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtGui.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionManual)
        self.menuHelp.addAction(self.actionAbout)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Waves", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Tab 2", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_As.setText(QtGui.QApplication.translate("MainWindow", "Save As", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionManual.setText(QtGui.QApplication.translate("MainWindow", "Manual", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setText(QtGui.QApplication.translate("MainWindow", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setText(QtGui.QApplication.translate("MainWindow", "Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo.setText(QtGui.QApplication.translate("MainWindow", "Undo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo.setText(QtGui.QApplication.translate("MainWindow", "Redo", None, QtGui.QApplication.UnicodeUTF8))

import resource_rc
