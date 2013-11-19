# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Dropbox\Coding\GameSelector\GameDetail.ui'
#
# Created: Tue Nov 19 17:31:33 2013
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

class Ui_GameDetail(object):
    def setupUi(self, GameDetail):
        GameDetail.setObjectName(_fromUtf8("GameDetail"))
        GameDetail.setWindowModality(QtCore.Qt.ApplicationModal)
        GameDetail.resize(1067, 593)
        self.closeButton = QtGui.QPushButton(GameDetail)
        self.closeButton.setGeometry(QtCore.QRect(990, 510, 75, 75))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy)
        self.closeButton.setMinimumSize(QtCore.QSize(0, 70))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.imageDisplay = QtWebKit.QWebView(GameDetail)
        self.imageDisplay.setGeometry(QtCore.QRect(0, 0, 500, 200))
        self.imageDisplay.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.imageDisplay.setObjectName(_fromUtf8("imageDisplay"))
        self.description = QtWebKit.QWebView(GameDetail)
        self.description.setGeometry(QtCore.QRect(530, 0, 500, 200))
        self.description.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.description.setObjectName(_fromUtf8("description"))
        self.votingData = QtGui.QTableWidget(GameDetail)
        self.votingData.setGeometry(QtCore.QRect(30, 260, 521, 291))
        self.votingData.setColumnCount(5)
        self.votingData.setObjectName(_fromUtf8("votingData"))
        self.votingData.setRowCount(0)

        self.retranslateUi(GameDetail)
        QtCore.QMetaObject.connectSlotsByName(GameDetail)

    def retranslateUi(self, GameDetail):
        GameDetail.setWindowTitle(_translate("GameDetail", "Dialog", None))
        self.closeButton.setText(_translate("GameDetail", "Close", None))

from PyQt4 import QtWebKit
