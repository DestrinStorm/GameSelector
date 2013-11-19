import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from GameSelector import *
from bggdata import *
from GameDetail import *
import CollectionFilter

class DetailPopup(QDialog, Ui_GameDetail):

	NUMPLAYERS, BEST, RECOMMENDED, NOTRECOMMENDED, TOTAL = range(5)

	def __init__(self,bggid,parent=None):
		super(DetailPopup,self).__init__(parent)
		self.ui=Ui_GameDetail()
		self.ui.setupUi(self)
		self.ui.description.setHtml(CollectionFilter.bgcollection[bggid]["description"])
		self.ui.imageDisplay.setHtml("...Loading image...")
		self.ui.imageDisplay.load(QUrl(CollectionFilter.bgcollection[bggid]["thumbnail"]))
		self.ui.closeButton.clicked.connect(self.done)
		self.ui.votingData.clear()
		self.ui.votingData.setSortingEnabled(False)
		#replace headers - clear() deletes them :(
		headers = ["Players", "Best", "Recommended", "Not Recommended", "Total"]
		self.ui.votingData.setHorizontalHeaderLabels(headers)
		#fetch voting data and populate table
		#clunky arsed way to get the suggestedplayercount values
		playercountlist = list(CollectionFilter.bgcollection[bggid]['suggestedplayercount'].keys())
		playercountlist.remove('totalvotes')
		self.ui.votingData.setRowCount(len(playercountlist))
		for row,playercount in enumerate(playercountlist):
			#numplayers column
			item = QTableWidgetItem(playercount)
			self.ui.votingData.setItem(row, self.NUMPLAYERS, item)
			#Best votes column
			#print(playercount)
			item = QTableWidgetItem(CollectionFilter.bgcollection[bggid].suggestedPlayerCountVoteRaw(playercount,'Best'))
			item.setTextAlignment(Qt.AlignCenter|Qt.AlignVCenter)
			self.ui.votingData.setItem(row, self.BEST, item)
		#reenable sorting
		self.ui.votingData.setSortingEnabled(True)
		#TODO: kinda want to keep track of whatever the 'current' sort is
		self.ui.votingData.sortItems(self.NUMPLAYERS)

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
		#wire up the list items
		self.ui.mechaniclist.itemClicked.connect(lambda: self.mechanicFilter())
		self.ui.categorylist.itemClicked.connect(lambda: self.categoryFilter())
		#wire the boardgame table up to the details popup
		self.ui.bgcollectionView.itemClicked.connect(lambda: self.showdetails(self.ui.bgcollectionView.item(self.ui.bgcollectionView.currentRow(),self.NAME).data(Qt.UserRole)))
		#and finally link in the admin screen
		self.ui.downloadData.clicked.connect(lambda: self.downloadData())		
		#size/format overrides not easily configurable from QTDesigner
		self.ui.bgcollectionView.verticalScrollBar().setStyleSheet("QScrollBar:vertical { width: 55px; }")
		self.ui.bgcollectionView.horizontalHeader().setMinimumHeight(50)
		self.ui.mechaniclist.verticalScrollBar().setStyleSheet("QScrollBar:vertical { width: 55px; }")
		self.ui.categorylist.verticalScrollBar().setStyleSheet("QScrollBar:vertical { width: 55px; }")
		self.ui.bgcollectionView.setColumnWidth(self.NAME,423)
		self.ui.bgcollectionView.setColumnWidth(self.MINPLAYERS,60)
		self.ui.bgcollectionView.setColumnWidth(self.MAXPLAYERS,60)
		self.ui.bgcollectionView.setColumnWidth(self.PLAYTIME,60)
		#Initial setup
		self.updateUI()

	def updateUI(self):
		CollectionFilter.combinefilters()
		self.populateLists()
		self.populateTable()		

	def populateLists(self):
		#populate mechanic/category lists with values
		#first, remember what we have selected
		selection = []
		for mechanism in self.ui.mechaniclist.selectedItems():
			selection.append(mechanism.text())
		#that is stored, clear and repopulate
		self.ui.mechaniclist.clear()
		for mechanic in CollectionFilter.mechanics:
			self.ui.mechaniclist.addItem(mechanic)
		self.ui.mechaniclist.sortItems()
		#now reselect previously selected items
		for mechanic in selection:
			for item in self.ui.mechaniclist.findItems(mechanic,Qt.MatchFixedString):
				item.setSelected(True)
		#and do the same for the category list
		selection = []
		for category in self.ui.categorylist.selectedItems():
			selection.append(category.text())
		self.ui.categorylist.clear()
		for category in CollectionFilter.categories:
			self.ui.categorylist.addItem(category)
		self.ui.categorylist.sortItems()
		for category in selection:
			for item in self.ui.categorylist.findItems(category,Qt.MatchFixedString):
				item.setSelected(True)
	
	def populateTable(self):
		#clear and disable sorting
		self.ui.bgcollectionView.clear()
		self.ui.bgcollectionView.setSortingEnabled(False)
		#replace headers - clear() deletes them :(
		headers = ["Name", "Min.\nPlayers", "Max.\nPlayers", "Playing\nTime"]
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
			self.ui.bestButton.setChecked(False)
			self.ui.recommendedButton.setChecked(False)
			self.ui.bestButton.setEnabled(False)
			self.ui.recommendedButton.setEnabled(False)
			CollectionFilter.resetplayerfilter()
			CollectionFilter.resetsuggestedfilter()
			self.updateUI()
		#are the suggested voting filters on?
		if self.ui.bestButton.isChecked():
			self.bestFilter(self.ui.bestButton)
		elif self.ui.recommendedButton.isChecked():
			self.recommendedFilter(self.ui.recommendedButton)
		else:
			self.updateUI()

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
		self.updateUI()

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
		self.updateUI()	
			
	def playtimeFilter(self,playtime,button):
		if button.isChecked():
			CollectionFilter.playtimefilter(playtime)
			turnoffset = self.playtimebuttonset.difference({button})
			for button in turnoffset:
				button.setChecked(False)
		else:
			CollectionFilter.resetplaytimefilter()
		self.updateUI()

	def mechanicFilter(self):
		selection = []
		for mechanism in self.ui.mechaniclist.selectedItems():
			selection.append(mechanism.text())
		CollectionFilter.mechanicfilter(selection)
		self.updateUI()
		
	def categoryFilter(self):
		selection = []
		for category in self.ui.categorylist.selectedItems():
			selection.append(category.text())
		CollectionFilter.categoryfilter(selection)
		self.updateUI()

	def downloadData(self):
		ret = QMessageBox.information(self, "Download", "Be warned, this locks up the screen for a good 10 mins.  Continue?",QMessageBox.Ok | QMessageBox.Cancel)
		if ret == QMessageBox.Ok:
			print("downloading")
			downloadCollection()
			CollectionFilter.loadCollection()
			CollectionFilter.resetAllFilters()
			#need a 'reset ui' function
			self.updateUI()

	def showdetails(self,selectedgameid):
		#display the details dialog, passing in the BGGID of the selected game
		dlg = DetailPopup(selectedgameid)
		dlg.exec_()
	
if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = MainForm()
	#Dis/Enable next line for frameless
	#form.setWindowFlags(form.windowFlags() | QtCore.Qt.FramelessWindowHint)
	form.showMaximized()
	sys.exit(app.exec_())
