import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from CollectionFilter import *
from GameSelector import *

NAME, MINPLAYERS, MAXPLAYERS, PLAYINGTIME = range(4)

class BGTableModel(QAbstractTableModel):
	def __init__(self):
		super(BGTableModel, self).__init__()
		self.bgcollection = []
		self.mechanics = set()
		self.categories = set()

	def data(self,index,value,role=Qt.DisplayRole):
		if not index.isValid() or not (0 <= index.row() < len(self.bgcollection)):
			return QVariant()
		boardgame = self.bgcollection[index.row()]
		column = index.column()
		if role == Qt.DisplayRole:
			if column == NAME:
				return boardgame["name"]
			elif column == MINPLAYERS:
				return int(boardgame["minplayers"])
			elif column == MAXPLAYERS:
				return QVariant(boardgame["maxplayers"])
			elif column == PLAYINGTIME:
				return QVariant(boardgame["playingtime"])
		elif role == Qt.TextAlignmentRole:
			if column == NAME:
				return QVariant(int(Qt.AlignLeft|Qt.AlignVCenter))
			return QVariant(int(Qt.AlignCenter|Qt.AlignVCenter))
		return QVariant()

	def rowCount(self, index=QModelIndex()):
		return len(self.bgcollection)                

	def columnCount(self, index=QModelIndex()):
		return 4

	def headerData(self, section, orientation, role=Qt.DisplayRole):
		if role == Qt.TextAlignmentRole:
			if orientation == Qt.Horizontal:
				return QVariant(int(Qt.AlignLeft|Qt.AlignVCenter))
			return QVariant(int(Qt.AlignCenter|Qt.AlignVCenter))
		if role != Qt.DisplayRole:
			return QVariant()
		if orientation == Qt.Horizontal:
			if section == NAME:
				return "Name"
			elif section == MINPLAYERS:
				return "Min. Players"
			elif section == MAXPLAYERS:
				return "Max. Players"
			elif section == PLAYINGTIME:
				return "Playing Time"
		return QVariant(int(section + 1))

class MainForm(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self,parent=None):
		QtGui.QWindow.__init__(self,parent)
		self.ui=Ui_MainWindow()
		self.ui.setupUi(self)
		#Initial setup
		datamodel = BGTableModel()
		for boardgame in bgcollection.keys():
			datamodel.bgcollection.append(bgcollection[boardgame])
		self.ui.bgcollectionView.setModel(datamodel)
		
if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	GSapp=MainForm()
	GSapp.show()
	sys.exit(app.exec_())
