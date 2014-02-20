# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/spencer/git/waves/forms/score_editor.ui'
#
# Created: Thu Feb 20 07:00:11 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ScoreEditor(object):
    def setupUi(self, ScoreEditor):
        ScoreEditor.setObjectName("ScoreEditor")
        ScoreEditor.resize(483, 403)
        self.verticalLayout = QtGui.QVBoxLayout(ScoreEditor)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = QtGui.QGraphicsView(ScoreEditor)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)

        self.retranslateUi(ScoreEditor)
        QtCore.QMetaObject.connectSlotsByName(ScoreEditor)

    def retranslateUi(self, ScoreEditor):
        ScoreEditor.setWindowTitle(QtGui.QApplication.translate("ScoreEditor", "Score Editor", None, QtGui.QApplication.UnicodeUTF8))

