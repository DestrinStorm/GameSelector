# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Dropbox\Coding\GameSelector\GameSelector.ui'
#
# Created: Sat Dec 21 21:30:30 2013
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
        GameSelector.resize(1819, 992)
        self.centralwidget = QtGui.QWidget(GameSelector)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.bgcollectionView = QtGui.QTableWidget(self.centralwidget)
        self.bgcollectionView.setGeometry(QtCore.QRect(828, 10, 981, 975))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.bgcollectionView.setFont(font)
        self.bgcollectionView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.bgcollectionView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.bgcollectionView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.bgcollectionView.setAlternatingRowColors(True)
        self.bgcollectionView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.bgcollectionView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.bgcollectionView.setRowCount(1)
        self.bgcollectionView.setColumnCount(4)
        self.bgcollectionView.setObjectName(_fromUtf8("bgcollectionView"))
        self.bgcollectionView.horizontalHeader().setDefaultSectionSize(50)
        self.bgcollectionView.horizontalHeader().setMinimumSectionSize(1)
        self.bgcollectionView.horizontalHeader().setSortIndicatorShown(True)
        self.bgcollectionView.verticalHeader().setVisible(False)
        self.lcdResults = QtGui.QLCDNumber(self.centralwidget)
        self.lcdResults.setGeometry(QtCore.QRect(730, 330, 91, 45))
        self.lcdResults.setDigitCount(3)
        self.lcdResults.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdResults.setObjectName(_fromUtf8("lcdResults"))
        self.numPlayerFrame = QtGui.QFrame(self.centralwidget)
        self.numPlayerFrame.setGeometry(QtCore.QRect(20, 10, 451, 311))
        self.numPlayerFrame.setFrameShape(QtGui.QFrame.Box)
        self.numPlayerFrame.setFrameShadow(QtGui.QFrame.Plain)
        self.numPlayerFrame.setObjectName(_fromUtf8("numPlayerFrame"))
        self.bestButton = QtGui.QPushButton(self.numPlayerFrame)
        self.bestButton.setEnabled(False)
        self.bestButton.setGeometry(QtCore.QRect(10, 10, 100, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.bestButton.setFont(font)
        self.bestButton.setCheckable(True)
        self.bestButton.setObjectName(_fromUtf8("bestButton"))
        self.numplayerLabel = QtGui.QLabel(self.numPlayerFrame)
        self.numplayerLabel.setGeometry(QtCore.QRect(119, 20, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.numplayerLabel.setFont(font)
        self.numplayerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.numplayerLabel.setObjectName(_fromUtf8("numplayerLabel"))
        self.recommendedButton = QtGui.QPushButton(self.numPlayerFrame)
        self.recommendedButton.setEnabled(False)
        self.recommendedButton.setGeometry(QtCore.QRect(249, 10, 191, 75))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.recommendedButton.setFont(font)
        self.recommendedButton.setCheckable(True)
        self.recommendedButton.setObjectName(_fromUtf8("recommendedButton"))
        self.Btn2Player = QtGui.QPushButton(self.numPlayerFrame)
        self.Btn2Player.setGeometry(QtCore.QRect(10, 90, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Btn2Player.setFont(font)
        self.Btn2Player.setCheckable(True)
        self.Btn2Player.setObjectName(_fromUtf8("Btn2Player"))
        self.Btn3Player = QtGui.QPushButton(self.numPlayerFrame)
        self.Btn3Player.setGeometry(QtCore.QRect(120, 90, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Btn3Player.setFont(font)
        self.Btn3Player.setCheckable(True)
        self.Btn3Player.setObjectName(_fromUtf8("Btn3Player"))
        self.Btn4Player = QtGui.QPushButton(self.numPlayerFrame)
        self.Btn4Player.setGeometry(QtCore.QRect(230, 90, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Btn4Player.setFont(font)
        self.Btn4Player.setCheckable(True)
        self.Btn4Player.setObjectName(_fromUtf8("Btn4Player"))
        self.Btn5Player = QtGui.QPushButton(self.numPlayerFrame)
        self.Btn5Player.setGeometry(QtCore.QRect(340, 90, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Btn5Player.setFont(font)
        self.Btn5Player.setCheckable(True)
        self.Btn5Player.setObjectName(_fromUtf8("Btn5Player"))
        self.Btn6Player = QtGui.QPushButton(self.numPlayerFrame)
        self.Btn6Player.setGeometry(QtCore.QRect(10, 200, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Btn6Player.setFont(font)
        self.Btn6Player.setCheckable(True)
        self.Btn6Player.setObjectName(_fromUtf8("Btn6Player"))
        self.Btn7Player = QtGui.QPushButton(self.numPlayerFrame)
        self.Btn7Player.setGeometry(QtCore.QRect(120, 200, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Btn7Player.setFont(font)
        self.Btn7Player.setCheckable(True)
        self.Btn7Player.setObjectName(_fromUtf8("Btn7Player"))
        self.Btn8Player = QtGui.QPushButton(self.numPlayerFrame)
        self.Btn8Player.setGeometry(QtCore.QRect(230, 200, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Btn8Player.setFont(font)
        self.Btn8Player.setCheckable(True)
        self.Btn8Player.setObjectName(_fromUtf8("Btn8Player"))
        self.Btn9Player = QtGui.QPushButton(self.numPlayerFrame)
        self.Btn9Player.setGeometry(QtCore.QRect(340, 200, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Btn9Player.setFont(font)
        self.Btn9Player.setCheckable(True)
        self.Btn9Player.setObjectName(_fromUtf8("Btn9Player"))
        self.playTimeFrame = QtGui.QFrame(self.centralwidget)
        self.playTimeFrame.setGeometry(QtCore.QRect(480, 10, 341, 311))
        self.playTimeFrame.setFrameShape(QtGui.QFrame.Box)
        self.playTimeFrame.setFrameShadow(QtGui.QFrame.Plain)
        self.playTimeFrame.setObjectName(_fromUtf8("playTimeFrame"))
        self.PlayTimeLabel = QtGui.QLabel(self.playTimeFrame)
        self.PlayTimeLabel.setGeometry(QtCore.QRect(15, 10, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.PlayTimeLabel.setFont(font)
        self.PlayTimeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PlayTimeLabel.setObjectName(_fromUtf8("PlayTimeLabel"))
        self.Btn30mins = QtGui.QPushButton(self.playTimeFrame)
        self.Btn30mins.setGeometry(QtCore.QRect(10, 90, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Btn30mins.setFont(font)
        self.Btn30mins.setCheckable(True)
        self.Btn30mins.setChecked(False)
        self.Btn30mins.setFlat(False)
        self.Btn30mins.setObjectName(_fromUtf8("Btn30mins"))
        self.Btn60mins = QtGui.QPushButton(self.playTimeFrame)
        self.Btn60mins.setGeometry(QtCore.QRect(120, 90, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Btn60mins.setFont(font)
        self.Btn60mins.setCheckable(True)
        self.Btn60mins.setObjectName(_fromUtf8("Btn60mins"))
        self.Btn90mins = QtGui.QPushButton(self.playTimeFrame)
        self.Btn90mins.setGeometry(QtCore.QRect(230, 90, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Btn90mins.setFont(font)
        self.Btn90mins.setCheckable(True)
        self.Btn90mins.setObjectName(_fromUtf8("Btn90mins"))
        self.Btn120mins = QtGui.QPushButton(self.playTimeFrame)
        self.Btn120mins.setGeometry(QtCore.QRect(10, 200, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Btn120mins.setFont(font)
        self.Btn120mins.setCheckable(True)
        self.Btn120mins.setObjectName(_fromUtf8("Btn120mins"))
        self.Btn150mins = QtGui.QPushButton(self.playTimeFrame)
        self.Btn150mins.setGeometry(QtCore.QRect(120, 200, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Btn150mins.setFont(font)
        self.Btn150mins.setCheckable(True)
        self.Btn150mins.setObjectName(_fromUtf8("Btn150mins"))
        self.Btn180mins = QtGui.QPushButton(self.playTimeFrame)
        self.Btn180mins.setGeometry(QtCore.QRect(230, 200, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Btn180mins.setFont(font)
        self.Btn180mins.setCheckable(True)
        self.Btn180mins.setObjectName(_fromUtf8("Btn180mins"))
        self.tabbedzone = QtGui.QTabWidget(self.centralwidget)
        self.tabbedzone.setGeometry(QtCore.QRect(20, 330, 801, 656))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.tabbedzone.setFont(font)
        self.tabbedzone.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabbedzone.setObjectName(_fromUtf8("tabbedzone"))
        self.mechtab = QtGui.QWidget()
        self.mechtab.setObjectName(_fromUtf8("mechtab"))
        self.mechaniclist = QtGui.QListWidget(self.mechtab)
        self.mechaniclist.setGeometry(QtCore.QRect(-1, -1, 801, 600))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.mechaniclist.setFont(font)
        self.mechaniclist.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.mechaniclist.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mechaniclist.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.mechaniclist.setIconSize(QtCore.QSize(0, 0))
        self.mechaniclist.setObjectName(_fromUtf8("mechaniclist"))
        self.tabbedzone.addTab(self.mechtab, _fromUtf8(""))
        self.cattab = QtGui.QWidget()
        self.cattab.setObjectName(_fromUtf8("cattab"))
        self.categorylist = QtGui.QListWidget(self.cattab)
        self.categorylist.setEnabled(True)
        self.categorylist.setGeometry(QtCore.QRect(-1, -1, 801, 600))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.categorylist.setFont(font)
        self.categorylist.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.categorylist.setObjectName(_fromUtf8("categorylist"))
        self.tabbedzone.addTab(self.cattab, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.downloadData = QtGui.QPushButton(self.tab)
        self.downloadData.setGeometry(QtCore.QRect(10, 10, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.downloadData.setFont(font)
        self.downloadData.setCheckable(False)
        self.downloadData.setChecked(False)
        self.downloadData.setFlat(False)
        self.downloadData.setObjectName(_fromUtf8("downloadData"))
        self.tabbedzone.addTab(self.tab, _fromUtf8(""))
        GameSelector.setCentralWidget(self.centralwidget)

        self.retranslateUi(GameSelector)
        self.tabbedzone.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(GameSelector)

    def retranslateUi(self, GameSelector):
        GameSelector.setWindowTitle(_translate("GameSelector", "Game Selector", None))
        self.bgcollectionView.setSortingEnabled(True)
        self.bestButton.setText(_translate("GameSelector", "Best", None))
        self.numplayerLabel.setText(_translate("GameSelector", "<html><head/><body><p>Players</p></body></html>", None))
        self.recommendedButton.setText(_translate("GameSelector", "Recommended", None))
        self.Btn2Player.setText(_translate("GameSelector", "2", None))
        self.Btn3Player.setText(_translate("GameSelector", "3", None))
        self.Btn4Player.setText(_translate("GameSelector", "4", None))
        self.Btn5Player.setText(_translate("GameSelector", "5", None))
        self.Btn6Player.setText(_translate("GameSelector", "6", None))
        self.Btn7Player.setText(_translate("GameSelector", "7", None))
        self.Btn8Player.setText(_translate("GameSelector", "8", None))
        self.Btn9Player.setText(_translate("GameSelector", "9", None))
        self.PlayTimeLabel.setText(_translate("GameSelector", "Playing Time", None))
        self.Btn30mins.setText(_translate("GameSelector", "0:30", None))
        self.Btn60mins.setText(_translate("GameSelector", "1:00", None))
        self.Btn90mins.setText(_translate("GameSelector", "1:30", None))
        self.Btn120mins.setText(_translate("GameSelector", "2:00", None))
        self.Btn150mins.setText(_translate("GameSelector", "2:30", None))
        self.Btn180mins.setText(_translate("GameSelector", "3:00", None))
        self.tabbedzone.setTabText(self.tabbedzone.indexOf(self.mechtab), _translate("GameSelector", "Mechanism", None))
        self.tabbedzone.setTabText(self.tabbedzone.indexOf(self.cattab), _translate("GameSelector", "Theme", None))
        self.downloadData.setText(_translate("GameSelector", "Download\n"
"Collection", None))
        self.tabbedzone.setTabText(self.tabbedzone.indexOf(self.tab), _translate("GameSelector", "Admin", None))

