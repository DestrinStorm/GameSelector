import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from GameSelector import *
import CollectionFilter

class MainForm(QtWidgets.QMainWindow, Ui_GameSelector):

	NAME, MINPLAYERS, MAXPLAYERS, PLAYTIME = range(4)
		
	def __init__(self,parent=None):
		QtGui.QWindow.__init__(self,parent)
		self.ui=Ui_GameSelector()
		self.ui.setupUi(self)
		#Wire up the player buttons to the filters
		self.ui.bestButton.clicked.connect(lambda: self.bestFilter(self.ui.bestButton))
		self.ui.recommendedButton.clicked.connect(lambda: self.recommendedFilter(self.ui.recommendedButton))
		self.ui.Btn1Player.clicked.connect(lambda: self.playerFilter(1,self.ui.Btn1Player))
		self.ui.Btn2Player.clicked.connect(lambda: self.playerFilter(2,self.ui.Btn2Player))
		self.ui.Btn3Player.clicked.connect(lambda: self.playerFilter(3,self.ui.Btn3Player))
		self.ui.Btn4Player.clicked.connect(lambda: self.playerFilter(4,self.ui.Btn4Player))
		self.ui.Btn5Player.clicked.connect(lambda: self.playerFilter(5,self.ui.Btn5Player))
		self.ui.Btn6Player.clicked.connect(lambda: self.playerFilter(6,self.ui.Btn6Player))
		self.ui.Btn7Player.clicked.connect(lambda: self.playerFilter(7,self.ui.Btn7Player))
		self.ui.Btn8Player.clicked.connect(lambda: self.playerFilter(8,self.ui.Btn8Player))
		self.ui.Btn9Player.clicked.connect(lambda: self.playerFilter(9,self.ui.Btn9Player))
		self.ui.Btn10Player.clicked.connect(lambda: self.playerFilter(10,self.ui.Btn10Player))
		self.buttonset = set()
		self.buttonset.add(self.ui.Btn1Player)
		self.buttonset.add(self.ui.Btn2Player)
		self.buttonset.add(self.ui.Btn3Player)
		self.buttonset.add(self.ui.Btn4Player)
		self.buttonset.add(self.ui.Btn5Player)
		self.buttonset.add(self.ui.Btn6Player)
		self.buttonset.add(self.ui.Btn7Player)
		self.buttonset.add(self.ui.Btn8Player)
		self.buttonset.add(self.ui.Btn9Player)
		self.buttonset.add(self.ui.Btn10Player)
		#set the playtime dial maximum and wire that in
		self.ui.playtimedial.setMaximum(CollectionFilter.longestplaytime)
		self.ui.playtimedial.valueChanged.connect(lambda: self.playtimeFilter(self.ui.playtimedial.value()))
		#Initial setup
		self.populateTable()
		self.ui.bgcollectionView.resizeColumnsToContents()

	def populateTable(self):
		#clear and disable sorting
		self.ui.bgcollectionView.clear()
		self.ui.bgcollectionView.setSortingEnabled(False)
		self.ui.bgcollectionView.setRowCount(len(CollectionFilter.filteredset))
		headers = ["Name", "Min. Players", "Max. Players", "Playing Time"]
		self.ui.bgcollectionView.setColumnCount(len(headers))
		self.ui.bgcollectionView.setHorizontalHeaderLabels(headers)
		for row, boardgame in enumerate(CollectionFilter.filteredset):
			#name column
			item = QTableWidgetItem(CollectionFilter.bgcollection[boardgame]["name"])
			item.setData(Qt.UserRole, QVariant(CollectionFilter.bgcollection[boardgame]["ID"]))
			self.ui.bgcollectionView.setItem(row, self.NAME, item)
			#minplayers column
			item = QTableWidgetItem(str.rjust(str(CollectionFilter.bgcollection[boardgame]["minplayers"]),2))
			item.setTextAlignment(Qt.AlignCenter|Qt.AlignVCenter)
			self.ui.bgcollectionView.setItem(row, self.MINPLAYERS, item)
			#maxplayers column
			item = QTableWidgetItem(str.rjust(str(CollectionFilter.bgcollection[boardgame]["maxplayers"]),2))
			item.setTextAlignment(Qt.AlignCenter|Qt.AlignVCenter)
			self.ui.bgcollectionView.setItem(row, self.MAXPLAYERS, item)
			#playingtime column
			item = QTableWidgetItem(str.rjust(str(CollectionFilter.bgcollection[boardgame]["playingtime"]),3))
			item.setTextAlignment(Qt.AlignCenter|Qt.AlignVCenter)
			self.ui.bgcollectionView.setItem(row, self.PLAYTIME, item)
		#reenable sorting
		self.ui.bgcollectionView.setSortingEnabled(True)
		#TODO: kinda want to keep track of whatever the 'current' sort is
		self.ui.bgcollectionView.sortItems(self.NAME)

	def playerFilter(self,numplayers,button):
		if button.isChecked():
			CollectionFilter.numplayerfilter(numplayers)
			turnoffset = self.buttonset.difference({button})
			for button in turnoffset:
				button.setChecked(False)
			self.ui.bestButton.setEnabled(True)
			self.ui.recommendedButton.setEnabled(True)
		else:
			CollectionFilter.resetplayerfilter()
			self.ui.bestButton.setEnabled(False)
			self.ui.recommendedButton.setEnabled(False)
		#are the suggested voting filters on?
		if self.ui.bestButton.isChecked():
			self.bestFilter(self.ui.bestButton)
		elif self.ui.recommendedButton.isChecked():
			self.recommendedFilter(self.ui.recommendedButton)
		else:
			CollectionFilter.combinefilters()
			self.populateTable()

	def bestFilter(self,button):
		if button.isChecked():
			#which player count is currently checked
			numplayers = 0
			for playercountbutton in self.buttonset:
				if playercountbutton.isChecked():
					numplayers = playercountbutton.text()		
			CollectionFilter.suggestedbestplayercountfilter(numplayers)
			self.ui.recommendedButton.setChecked(False)
		else:
			CollectionFilter.resetsuggestedfilter()
		CollectionFilter.combinefilters()
		self.populateTable()

	def recommendedFilter(self,button):
		if button.isChecked():
			#which player count is currently checked
			numplayers = 0
			for playercountbutton in self.buttonset:
				if playercountbutton.isChecked():
					numplayers = playercountbutton.text()		
			CollectionFilter.suggestedrecommendedplayercountfilter(numplayers)
			self.ui.bestButton.setChecked(False)
		else:
			CollectionFilter.resetsuggestedfilter()
		CollectionFilter.combinefilters()
		self.populateTable()	
			
	def playtimeFilter(self,playtime):
		if playtime == 0:
			CollectionFilter.resetplaytimefilter()
		else:
			CollectionFilter.playtimefilter(playtime)
		CollectionFilter.combinefilters()
		self.populateTable()
	
if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	form=MainForm()
	#Dis/Enable next line for frameless
	#form.setWindowFlags(form.windowFlags() | QtCore.Qt.FramelessWindowHint)
	form.show()
	sys.exit(app.exec_())
