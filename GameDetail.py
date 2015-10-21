# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GameDetail.ui'
#
# Created: Wed Oct 21 22:31:13 2015
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_GameDetail(object):
    def setupUi(self, GameDetail):
        GameDetail.setObjectName(_fromUtf8("GameDetail"))
        GameDetail.setWindowModality(QtCore.Qt.ApplicationModal)
        GameDetail.resize(1365, 744)
        self.closeButton = QtGui.QPushButton(GameDetail)
        self.closeButton.setGeometry(QtCore.QRect(1249, 409, 110, 331))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy)
        self.closeButton.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.closeButton.setFont(font)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.imageDisplay = QtWebKit.QWebView(GameDetail)
        self.imageDisplay.setGeometry(QtCore.QRect(10, 50, 520, 520))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.imageDisplay.setPalette(palette)
        self.imageDisplay.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.imageDisplay.setObjectName(_fromUtf8("imageDisplay"))
        self.description = QtWebKit.QWebView(GameDetail)
        self.description.setGeometry(QtCore.QRect(540, 50, 821, 351))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.description.setFont(font)
        self.description.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.description.setObjectName(_fromUtf8("description"))
        self.votingData = QtGui.QTableWidget(GameDetail)
        self.votingData.setGeometry(QtCore.QRect(540, 450, 701, 291))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.votingData.setFont(font)
        self.votingData.setColumnCount(4)
        self.votingData.setObjectName(_fromUtf8("votingData"))
        self.votingData.setRowCount(0)
        self.bgName = QtGui.QLabel(GameDetail)
        self.bgName.setGeometry(QtCore.QRect(5, 2, 1351, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.bgName.setFont(font)
        self.bgName.setTextFormat(QtCore.Qt.PlainText)
        self.bgName.setAlignment(QtCore.Qt.AlignCenter)
        self.bgName.setObjectName(_fromUtf8("bgName"))
        self.voteLabel = QtGui.QLabel(GameDetail)
        self.voteLabel.setGeometry(QtCore.QRect(540, 410, 701, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.voteLabel.setFont(font)
        self.voteLabel.setTextFormat(QtCore.Qt.PlainText)
        self.voteLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.voteLabel.setObjectName(_fromUtf8("voteLabel"))

        self.retranslateUi(GameDetail)
        QtCore.QMetaObject.connectSlotsByName(GameDetail)

    def retranslateUi(self, GameDetail):
        GameDetail.setWindowTitle(_translate("GameDetail", "Dialog", None))
        self.closeButton.setText(_translate("GameDetail", "Close", None))
        self.bgName.setText(_translate("GameDetail", "Ticket to Ride Map Collection: Volume 1 - Team Asia & Legendary Asia", None))
        self.voteLabel.setText(_translate("GameDetail", "Number of Players Voting Data", None))

from PyQt4 import QtWebKit
