import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from GameSelector import *
from bggdata import *
import CollectionFilter

class MainForm(QMainWindow, Ui_GameSelector):

	NAME, MINPLAYERS, MAXPLAYERS, PLAYTIME = range(4)
		
	def __init__(self,parent=None):
		super(MainForm, self).__init__(parent)
		self.ui=Ui_GameSelector()
		self.ui.setupUi(self)
		#Wire up the player buttons to the filters
		self.ui.bestButton.clicked.connect(lambda: self.bestFilter(self.ui.bestButton))
		self.ui.recommendedButton.clicked.connect(lambda: self.recommendedFilter(self.ui.recommendedButton))
		self.ui.Btn2Player.clicked.connect(lambda: self.playerFilter(2,self.ui.Btn2Player))
		self.ui.Btn3Player.clicked.connect(lambda: self.playerFilter(3,self.ui.Btn3Player))
		self.ui.Btn4Player.clicked.connect(lambda: self.playerFilter(4,self.ui.Btn4Player))
		self.ui.Btn5Player.clicked.connect(lambda: self.playerFilter(5,self.ui.Btn5Player))
		self.ui.Btn6Player.clicked.connect(lambda: self.playerFilter(6,self.ui.Btn6Player))
		self.ui.Btn7Player.clicked.connect(lambda: self.playerFilter(7,self.ui.Btn7Player))
		self.ui.Btn8Player.clicked.connect(lambda: self.playerFilter(8,self.ui.Btn8Player))
		self.ui.Btn9Player.clicked.connect(lambda: self.playerFilter(9,self.ui.Btn9Player))
		self.playercountbuttonset = set()
		self.playercountbuttonset.add(self.ui.Btn2Player)
		self.playercountbuttonset.add(self.ui.Btn3Player)
		self.playercountbuttonset.add(self.ui.Btn4Player)
		self.playercountbuttonset.add(self.ui.Btn5Player)
		self.playercountbuttonset.add(self.ui.Btn6Player)
		self.playercountbuttonset.add(self.ui.Btn7Player)
		self.playercountbuttonset.add(self.ui.Btn8Player)
		self.playercountbuttonset.add(self.ui.Btn9Player)
		#wire up the playtime buttons
		self.ui.Btn30mins.clicked.connect(lambda: self.playtimeFilter(30,self.ui.Btn30mins))
		self.ui.Btn60mins.clicked.connect(lambda: self.playtimeFilter(60,self.ui.Btn60mins))
		self.ui.Btn90mins.clicked.connect(lambda: self.playtimeFilter(90,self.ui.Btn90mins))
		self.ui.Btn120mins.clicked.connect(lambda: self.playtimeFilter(120,self.ui.Btn120mins))
		self.ui.Btn150mins.clicked.connect(lambda: self.playtimeFilter(150,self.ui.Btn150mins))
		self.ui.Btn180mins.clicked.connect(lambda: self.playtimeFilter(180,self.ui.Btn180mins))
		self.ui.Btn240mins.clicked.connect(lambda: self.playtimeFilter(240,self.ui.Btn240mins))
		self.ui.Btn300mins.clicked.connect(lambda: self.playtimeFilter(300,self.ui.Btn300mins))
		self.playtimebuttonset = set()
		self.playtimebuttonset.add(self.ui.Btn30mins)
		self.playtimebuttonset.add(self.ui.Btn60mins)
		self.playtimebuttonset.add(self.ui.Btn90mins)
		self.playtimebuttonset.add(self.ui.Btn120mins)
		self.playtimebuttonset.add(self.ui.Btn150mins)
		self.playtimebuttonset.add(self.ui.Btn180mins)
		self.playtimebuttonset.add(self.ui.Btn240mins)
		self.playtimebuttonset.add(self.ui.Btn300mins)
		#wire in the mechanism/category buttons
		self.ui.mechButton.clicked.connect(lambda: self.mechcatbuttonfaff(self.ui.catButton,self.ui.mechButton))
		self.ui.catButton.clicked.connect(lambda: self.mechcatbuttonfaff(self.ui.mechButton,self.ui.catButton))
		#self.ui.catButton.clicked.connect(lambda: self.ui.mechButton.setEnabled(not(self.ui.catButton.isEnabled())))
		#size/format overrides not easily configurable from QTDesigner
		self.ui.bgcollectionView.verticalScrollBar().setStyleSheet("QScrollBar:vertical { width: 55px; }")
		self.ui.bgcollectionView.horizontalHeader().setMinimumHeight(50)
		self.ui.mechaniclist.verticalScrollBar().setStyleSheet("QScrollBar:vertical { width: 55px; }")
		self.ui.categorylist.verticalScrollBar().setStyleSheet("QScrollBar:vertical { width: 55px; }")
		self.ui.categorylist.setVisible(False)
		#populate mechanic/category lists
		for mechanic in CollectionFilter.mechanics:
			self.ui.mechaniclist.addItem(mechanic)
		self.ui.mechaniclist.sortItems()
		for category in CollectionFilter.categories:
			self.ui.categorylist.addItem(category)
		self.ui.categorylist.sortItems()
		self.ui.bgcollectionView.setColumnWidth(self.NAME,400)
		self.ui.bgcollectionView.setColumnWidth(self.MINPLAYERS,50)
		self.ui.bgcollectionView.setColumnWidth(self.MAXPLAYERS,50)
		self.ui.bgcollectionView.setColumnWidth(self.PLAYTIME,50)
		#Initial setup
		self.populateTable()		

	def mechcatbuttonfaff(self,buttontoenable,buttontodisable):
		#buttontodisable.setChecked(False)
		buttontodisable.setEnabled(False)
		buttontoenable.setChecked(False)
		buttontoenable.setEnabled(True)
	
	def populateTable(self):
		#clear and disable sorting
		self.ui.bgcollectionView.clear()
		self.ui.bgcollectionView.setSortingEnabled(False)
		#replace headers - clear() deletes them :(
		headers = ["Name", "Min.\nPlayers", "Max.\nPlayers", "Playing\nTime"]
		self.ui.bgcollectionView.setColumnCount(len(headers))
		self.ui.bgcollectionView.setHorizontalHeaderLabels(headers)
		#get the filtered list length and start populating
		self.ui.bgcollectionView.setRowCount(len(CollectionFilter.filteredset))
		for row, boardgame in enumerate(CollectionFilter.filteredset):
			#name column
			item = QTableWidgetItem(CollectionFilter.bgcollection[boardgame]["name"])
			item.setData(Qt.UserRole, CollectionFilter.bgcollection[boardgame]["ID"])
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
		#update the results LCD
		self.ui.lcdResults.display(self.ui.bgcollectionView.rowCount())

	def playerFilter(self,numplayers,button):
		if button.isChecked():
			CollectionFilter.numplayerfilter(numplayers)
			turnoffset = self.playercountbuttonset.difference({button})
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
			for playercountbutton in self.playercountbuttonset:
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
			for playercountbutton in self.playercountbuttonset:
				if playercountbutton.isChecked():
					numplayers = playercountbutton.text()		
			CollectionFilter.suggestedrecommendedplayercountfilter(numplayers)
			self.ui.bestButton.setChecked(False)
		else:
			CollectionFilter.resetsuggestedfilter()
		CollectionFilter.combinefilters()
		self.populateTable()	
			
	def playtimeFilter(self,playtime,button):
		if button.isChecked():
			CollectionFilter.playtimefilter(playtime)
			turnoffset = self.playtimebuttonset.difference({button})
			for button in turnoffset:
				button.setChecked(False)
		else:
			CollectionFilter.resetplaytimefilter()
		CollectionFilter.combinefilters()
		self.populateTable()
	
if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = MainForm()
	#Dis/Enable next line for frameless
	#form.setWindowFlags(form.windowFlags() | QtCore.Qt.FramelessWindowHint)
	form.showMaximized()
	sys.exit(app.exec_())
