# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/spencer/git/waves/forms/main_window.ui'
#
# Created: Sun Feb 23 07:57:43 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
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
        self.actionClose_Current_Score = QtGui.QAction(MainWindow)
        self.actionClose_Current_Score.setObjectName("actionClose_Current_Score")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose_Current_Score)
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
        MainWindow.setWindowTitle(
            QtGui.QApplication.translate(
                "MainWindow", "Waves", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab),
            QtGui.QApplication.translate(
                "MainWindow", "Tab 1", None, QtGui.QApplication.UnicodeUTF8
            ),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2),
            QtGui.QApplication.translate(
                "MainWindow", "Tab 2", None, QtGui.QApplication.UnicodeUTF8
            ),
        )
        self.menuFile.setTitle(
            QtGui.QApplication.translate(
                "MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.menuHelp.setTitle(
            QtGui.QApplication.translate(
                "MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.menuEdit.setTitle(
            QtGui.QApplication.translate(
                "MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.actionNew.setText(
            QtGui.QApplication.translate(
                "MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.actionNew.setShortcut(
            QtGui.QApplication.translate(
                "MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.actionOpen.setText(
            QtGui.QApplication.translate(
                "MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.actionOpen.setShortcut(
            QtGui.QApplication.translate(
                "MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.actionSave.setText(
            QtGui.QApplication.translate(
                "MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.actionSave.setShortcut(
            QtGui.QApplication.translate(
                "MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.actionSave_As.setText(
            QtGui.QApplication.translate(
                "MainWindow", "Save As", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.actionSave_As.setShortcut(
            QtGui.QApplication.translate(
                "MainWindow", "Ctrl+Shift+S", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.actionQuit.setText(
            QtGui.QApplication.translate(
                "MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.actionManual.setText(
            QtGui.QApplication.translate(
                "MainWindow", "Manual", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.actionAbout.setText(
            QtGui.QApplication.translate(
                "MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.actionCut.setText(
            QtGui.QApplication.translate(
                "MainWindow", "Cut", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.actionCopy.setText(
            QtGui.QApplication.translate(
                "MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.actionPaste.setText(
            QtGui.QApplication.translate(
                "MainWindow", "Paste", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.actionUndo.setText(
            QtGui.QApplication.translate(
                "MainWindow", "Undo", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.actionRedo.setText(
            QtGui.QApplication.translate(
                "MainWindow", "Redo", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.actionClose_Current_Score.setText(
            QtGui.QApplication.translate(
                "MainWindow",
                "Close Current Score",
                None,
                QtGui.QApplication.UnicodeUTF8,
            )
        )
        self.actionClose_Current_Score.setShortcut(
            QtGui.QApplication.translate(
                "MainWindow", "Ctrl+W", None, QtGui.QApplication.UnicodeUTF8
            )
        )


import resource_rc
