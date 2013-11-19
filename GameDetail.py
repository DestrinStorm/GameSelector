# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Dropbox\Coding\GameSelector\GameDetail.ui'
#
# Created: Tue Nov 19 14:21:02 2013
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
        self.gridLayoutWidget = QtGui.QWidget(GameDetail)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 1061, 591))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.description = QtWebKit.QWebView(self.gridLayoutWidget)
        self.description.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.description.setObjectName(_fromUtf8("description"))
        self.gridLayout.addWidget(self.description, 0, 1, 1, 1)
        self.imageDisplay = QtWebKit.QWebView(self.gridLayoutWidget)
        self.imageDisplay.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.imageDisplay.setObjectName(_fromUtf8("imageDisplay"))
        self.gridLayout.addWidget(self.imageDisplay, 0, 0, 1, 1)
        self.closeButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.gridLayout.addWidget(self.closeButton, 1, 1, 1, 1)

        self.retranslateUi(GameDetail)
        QtCore.QMetaObject.connectSlotsByName(GameDetail)

    def retranslateUi(self, GameDetail):
        GameDetail.setWindowTitle(_translate("GameDetail", "Dialog", None))
        self.closeButton.setText(_translate("GameDetail", "Close", None))

from PyQt4 import QtWebKit
