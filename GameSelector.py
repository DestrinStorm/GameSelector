# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Dropbox\Coding\GameSelector\GameSelector.ui'
#
# Created: Wed Nov 13 23:36:04 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_GameSelector(object):
    def setupUi(self, GameSelector):
        GameSelector.setObjectName(_fromUtf8("GameSelector"))
        GameSelector.setEnabled(True)
        GameSelector.resize(1185, 658)
        self.centralwidget = QtGui.QWidget(GameSelector)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.bgcollectionView = QtGui.QTableWidget(self.centralwidget)
        self.bgcollectionView.setGeometry(QtCore.QRect(270, 0, 915, 658))
        self.bgcollectionView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.bgcollectionView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.bgcollectionView.setAlternatingRowColors(True)
        self.bgcollectionView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.bgcollectionView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.bgcollectionView.setRowCount(1)
        self.bgcollectionView.setColumnCount(4)
        self.bgcollectionView.setObjectName(_fromUtf8("bgcollectionView"))
        self.bgcollectionView.horizontalHeader().setSortIndicatorShown(False)
        self.bgcollectionView.verticalHeader().setVisible(False)
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(5, 460, 260, 192))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(150, 340, 51, 31))
        self.lcdNumber.setDigitCount(3)
        self.lcdNumber.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.numPlayerFrame = QtGui.QFrame(self.centralwidget)
        self.numPlayerFrame.setGeometry(QtCore.QRect(5, 5, 260, 150))
        self.numPlayerFrame.setFrameShape(QtGui.QFrame.Box)
        self.numPlayerFrame.setFrameShadow(QtGui.QFrame.Plain)
        self.numPlayerFrame.setObjectName(_fromUtf8("numPlayerFrame"))
        self.bestButton = QtGui.QPushButton(self.numPlayerFrame)
        self.bestButton.setEnabled(False)
        self.bestButton.setGeometry(QtCore.QRect(10, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.bestButton.setFont(font)
        self.bestButton.setCheckable(True)
        self.bestButton.setObjectName(_fromUtf8("bestButton"))
        self.numplayerLabel = QtGui.QLabel(self.numPlayerFrame)
        self.numplayerLabel.setGeometry(QtCore.QRect(75, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.numplayerLabel.setFont(font)
        self.numplayerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.numplayerLabel.setObjectName(_fromUtf8("numplayerLabel"))
        self.recommendedButton = QtGui.QPushButton(self.numPlayerFrame)
        self.recommendedButton.setEnabled(False)
        self.recommendedButton.setGeometry(QtCore.QRect(160, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.recommendedButton.setFont(font)
        self.recommendedButton.setCheckable(True)
        self.recommendedButton.setObjectName(_fromUtf8("recommendedButton"))
        self.Btn1Player = QtGui.QPushButton(self.numPlayerFrame)
        self.Btn1Player.setGeometry(QtCore.QRect(10, 50, 41, 41))
        self.Btn1Player.setCheckable(True)
        self.Btn1Player.setChecked(False)
        self.Btn1Player.setFlat(False)
        self.Btn1Player.setObjectName(_fromUtf8("Btn1Player"))
        self.Btn2Player = QtGui.QPushButton(self.numPlayerFrame)
        self.Btn2Player.setGeometry(QtCore.QRect(60, 50, 41, 41))
        self.Btn2Player.setCheckable(True)
        self.Btn2Player.setObjectName(_fromUtf8("Btn2Player"))
        self.Btn3Player = QtGui.QPushButton(self.numPlayerFrame)
        self.Btn3Player.setGeometry(QtCore.QRect(110, 50, 41, 41))
        self.Btn3Player.setCheckable(True)
        self.Btn3Player.setObjectName(_fromUtf8("Btn3Player"))
        self.Btn4Player = QtGui.QPushButton(self.numPlayerFrame)
        self.Btn4Player.setGeometry(QtCore.QRect(160, 50, 41, 41))
        self.Btn4Player.setCheckable(True)
        self.Btn4Player.setObjectName(_fromUtf8("Btn4Player"))
        self.Btn5Player = QtGui.QPushButton(self.numPlayerFrame)
        self.Btn5Player.setGeometry(QtCore.QRect(210, 50, 41, 41))
        self.Btn5Player.setCheckable(True)
        self.Btn5Player.setObjectName(_fromUtf8("Btn5Player"))
        self.Btn6Player = QtGui.QPushButton(self.numPlayerFrame)
        self.Btn6Player.setGeometry(QtCore.QRect(10, 100, 41, 41))
        self.Btn6Player.setCheckable(True)
        self.Btn6Player.setObjectName(_fromUtf8("Btn6Player"))
        self.Btn7Player = QtGui.QPushButton(self.numPlayerFrame)
        self.Btn7Player.setGeometry(QtCore.QRect(60, 100, 41, 41))
        self.Btn7Player.setCheckable(True)
        self.Btn7Player.setObjectName(_fromUtf8("Btn7Player"))
        self.Btn8Player = QtGui.QPushButton(self.numPlayerFrame)
        self.Btn8Player.setGeometry(QtCore.QRect(110, 100, 41, 41))
        self.Btn8Player.setCheckable(True)
        self.Btn8Player.setObjectName(_fromUtf8("Btn8Player"))
        self.Btn9Player = QtGui.QPushButton(self.numPlayerFrame)
        self.Btn9Player.setGeometry(QtCore.QRect(160, 100, 41, 41))
        self.Btn9Player.setCheckable(True)
        self.Btn9Player.setObjectName(_fromUtf8("Btn9Player"))
        self.Btn10Player = QtGui.QPushButton(self.numPlayerFrame)
        self.Btn10Player.setGeometry(QtCore.QRect(210, 100, 41, 41))
        self.Btn10Player.setCheckable(True)
        self.Btn10Player.setObjectName(_fromUtf8("Btn10Player"))
        self.playTimeFrame = QtGui.QFrame(self.centralwidget)
        self.playTimeFrame.setGeometry(QtCore.QRect(5, 160, 260, 131))
        self.playTimeFrame.setFrameShape(QtGui.QFrame.Box)
        self.playTimeFrame.setFrameShadow(QtGui.QFrame.Plain)
        self.playTimeFrame.setObjectName(_fromUtf8("playTimeFrame"))
        self.PlayTimeLabel = QtGui.QLabel(self.playTimeFrame)
        self.PlayTimeLabel.setGeometry(QtCore.QRect(75, 10, 91, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PlayTimeLabel.setFont(font)
        self.PlayTimeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PlayTimeLabel.setObjectName(_fromUtf8("PlayTimeLabel"))
        self.Btn30mins = QtGui.QPushButton(self.playTimeFrame)
        self.Btn30mins.setGeometry(QtCore.QRect(10, 30, 41, 41))
        self.Btn30mins.setCheckable(True)
        self.Btn30mins.setChecked(False)
        self.Btn30mins.setFlat(False)
        self.Btn30mins.setObjectName(_fromUtf8("Btn30mins"))
        self.Btn60mins = QtGui.QPushButton(self.playTimeFrame)
        self.Btn60mins.setGeometry(QtCore.QRect(60, 30, 41, 41))
        self.Btn60mins.setCheckable(True)
        self.Btn60mins.setObjectName(_fromUtf8("Btn60mins"))
        self.Btn90mins = QtGui.QPushButton(self.playTimeFrame)
        self.Btn90mins.setGeometry(QtCore.QRect(110, 30, 41, 41))
        self.Btn90mins.setCheckable(True)
        self.Btn90mins.setObjectName(_fromUtf8("Btn90mins"))
        self.Btn120mins = QtGui.QPushButton(self.playTimeFrame)
        self.Btn120mins.setGeometry(QtCore.QRect(160, 30, 41, 41))
        self.Btn120mins.setCheckable(True)
        self.Btn120mins.setObjectName(_fromUtf8("Btn120mins"))
        self.Btn150mins = QtGui.QPushButton(self.playTimeFrame)
        self.Btn150mins.setGeometry(QtCore.QRect(210, 30, 41, 41))
        self.Btn150mins.setCheckable(True)
        self.Btn150mins.setObjectName(_fromUtf8("Btn150mins"))
        self.Btn180mins = QtGui.QPushButton(self.playTimeFrame)
        self.Btn180mins.setGeometry(QtCore.QRect(10, 80, 41, 41))
        self.Btn180mins.setCheckable(True)
        self.Btn180mins.setObjectName(_fromUtf8("Btn180mins"))
        self.Btn240mins = QtGui.QPushButton(self.playTimeFrame)
        self.Btn240mins.setGeometry(QtCore.QRect(60, 80, 41, 41))
        self.Btn240mins.setCheckable(True)
        self.Btn240mins.setObjectName(_fromUtf8("Btn240mins"))
        self.Btn300mins = QtGui.QPushButton(self.playTimeFrame)
        self.Btn300mins.setGeometry(QtCore.QRect(110, 80, 41, 41))
        self.Btn300mins.setCheckable(True)
        self.Btn300mins.setObjectName(_fromUtf8("Btn300mins"))
        self.Btn360mins = QtGui.QPushButton(self.playTimeFrame)
        self.Btn360mins.setGeometry(QtCore.QRect(160, 80, 41, 41))
        self.Btn360mins.setCheckable(True)
        self.Btn360mins.setObjectName(_fromUtf8("Btn360mins"))
        self.Btn420mins = QtGui.QPushButton(self.playTimeFrame)
        self.Btn420mins.setGeometry(QtCore.QRect(210, 80, 41, 41))
        self.Btn420mins.setCheckable(True)
        self.Btn420mins.setObjectName(_fromUtf8("Btn420mins"))
        GameSelector.setCentralWidget(self.centralwidget)

        self.retranslateUi(GameSelector)
        QtCore.QMetaObject.connectSlotsByName(GameSelector)

    def retranslateUi(self, GameSelector):
        GameSelector.setWindowTitle(_translate("GameSelector", "Game Selector", None))
        self.bgcollectionView.setSortingEnabled(True)
        self.bestButton.setText(_translate("GameSelector", "\'Best\'", None))
        self.numplayerLabel.setText(_translate("GameSelector", "Number of\n"
"Players", None))
        self.recommendedButton.setText(_translate("GameSelector", "\'Recommended\'", None))
        self.Btn1Player.setText(_translate("GameSelector", "1", None))
        self.Btn2Player.setText(_translate("GameSelector", "2", None))
        self.Btn3Player.setText(_translate("GameSelector", "3", None))
        self.Btn4Player.setText(_translate("GameSelector", "4", None))
        self.Btn5Player.setText(_translate("GameSelector", "5", None))
        self.Btn6Player.setText(_translate("GameSelector", "6", None))
        self.Btn7Player.setText(_translate("GameSelector", "7", None))
        self.Btn8Player.setText(_translate("GameSelector", "8", None))
        self.Btn9Player.setText(_translate("GameSelector", "9", None))
        self.Btn10Player.setText(_translate("GameSelector", "10", None))
        self.PlayTimeLabel.setText(_translate("GameSelector", "Playing Time", None))
        self.Btn30mins.setText(_translate("GameSelector", "0:30", None))
        self.Btn60mins.setText(_translate("GameSelector", "1:00", None))
        self.Btn90mins.setText(_translate("GameSelector", "1:30", None))
        self.Btn120mins.setText(_translate("GameSelector", "2:00", None))
        self.Btn150mins.setText(_translate("GameSelector", "2:30", None))
        self.Btn180mins.setText(_translate("GameSelector", "3:00", None))
        self.Btn240mins.setText(_translate("GameSelector", "4:00", None))
        self.Btn300mins.setText(_translate("GameSelector", "5:00", None))
        self.Btn360mins.setText(_translate("GameSelector", "6:00", None))
        self.Btn420mins.setText(_translate("GameSelector", "7:00", None))

