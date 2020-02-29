# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GameDetail.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GameDetail(object):
    def setupUi(self, GameDetail):
        GameDetail.setObjectName("GameDetail")
        GameDetail.setWindowModality(QtCore.Qt.ApplicationModal)
        GameDetail.resize(1365, 744)
        self.closeButton = QtWidgets.QPushButton(GameDetail)
        self.closeButton.setGeometry(QtCore.QRect(1249, 409, 110, 331))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy)
        self.closeButton.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.closeButton.setFont(font)
        self.closeButton.setObjectName("closeButton")
        self.votingData = QtWidgets.QTableWidget(GameDetail)
        self.votingData.setGeometry(QtCore.QRect(540, 450, 701, 291))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.votingData.setFont(font)
        self.votingData.setColumnCount(4)
        self.votingData.setObjectName("votingData")
        self.votingData.setRowCount(0)
        self.bgName = QtWidgets.QLabel(GameDetail)
        self.bgName.setGeometry(QtCore.QRect(5, 2, 1351, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.bgName.setFont(font)
        self.bgName.setTextFormat(QtCore.Qt.PlainText)
        self.bgName.setAlignment(QtCore.Qt.AlignCenter)
        self.bgName.setObjectName("bgName")
        self.voteLabel = QtWidgets.QLabel(GameDetail)
        self.voteLabel.setGeometry(QtCore.QRect(540, 410, 701, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.voteLabel.setFont(font)
        self.voteLabel.setTextFormat(QtCore.Qt.PlainText)
        self.voteLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.voteLabel.setObjectName("voteLabel")
        self.description = QtWidgets.QTextBrowser(GameDetail)
        self.description.setGeometry(QtCore.QRect(5, 41, 521, 701))
        self.description.setObjectName("description")

        self.retranslateUi(GameDetail)
        QtCore.QMetaObject.connectSlotsByName(GameDetail)

    def retranslateUi(self, GameDetail):
        _translate = QtCore.QCoreApplication.translate
        GameDetail.setWindowTitle(_translate("GameDetail", "Dialog"))
        self.closeButton.setText(_translate("GameDetail", "Close"))
        self.bgName.setText(_translate("GameDetail", "Ticket to Ride Map Collection: Volume 1 - Team Asia & Legendary Asia"))
        self.voteLabel.setText(_translate("GameDetail", "Number of Players Voting Data"))

