# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/spencer/git/waves/forms/score_editor.ui'
#
# Created: Sun Feb 23 07:57:43 2014
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
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setContentsMargins(7, 7, 7, 7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtGui.QPushButton(ScoreEditor)
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/icons/Media-Play-48.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalSlider = QtGui.QSlider(ScoreEditor)
        self.horizontalSlider.setStyleSheet("")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout.addWidget(self.horizontalSlider)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.graphicsView = QtGui.QGraphicsView(ScoreEditor)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(ScoreEditor)
        QtCore.QMetaObject.connectSlotsByName(ScoreEditor)

    def retranslateUi(self, ScoreEditor):
        ScoreEditor.setWindowTitle(
            QtGui.QApplication.translate(
                "ScoreEditor", "Score Editor", None, QtGui.QApplication.UnicodeUTF8
            )
        )


import resource_rc
