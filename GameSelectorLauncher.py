import sys
import os
import pickle
import time
import xml.etree.ElementTree as etree
from urllib.request import urlopen
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from GameSelector import *
from GameDetail import *

#Define the boardgame class
#Extend dictionary and assign the appropriate data to preset key names
class boardgamedict(dict):
	def __init__(self, ID, name, minplayers, maxplayers, minplaytime, maxplaytime, description='', thumbnail='', image='', suggestedplayercount=dict(),categories=list(),mechanics=list()):
		dict.__init__({})
		self["ID"] = int(ID)
		self["name"] = name
		self["minplayers"] = int(minplayers)
		self["maxplayers"] = int(maxplayers)
		self["minplaytime"] = int(minplaytime)
		self["maxplaytime"] = int(maxplaytime)
		self["description"] = description
		self["thumbnail"] = thumbnail
		self["image"] = image
		self["suggestedplayercount"] = suggestedplayercount
		self["categories"] = categories
		self["mechanics"] = mechanics

	def suggestedPlayerCountVote(self,playercount,votetype='Best'):
		if playercount in self['suggestedplayercount'].keys():
			bestvotes = self['suggestedplayercount'][playercount][votetype]
			totalvotes = self['suggestedplayercount']['totalvotes']
			if totalvotes == 0:
				#no votes yet :(
				return 0
			percentage = (bestvotes / totalvotes) * 100
			return round(percentage)
		else:
			return 0

	def suggestedPlayerCountVoteRaw(self,playercount,votetype='Best'):
		if playercount in self['suggestedplayercount'].keys():
			bestvotes = self['suggestedplayercount'][playercount][votetype]
			return str(bestvotes)
		else:
			return 0

	def suggestedPlayerCountVoteTotal(self,playercount):
		if playercount in self['suggestedplayercount'].keys():
			totalvotes = self['suggestedplayercount']['totalvotes']
			return str(totalvotes)
		else:
			return 0
		
	def isBestWith(self,playercount,votetolerance=50):
		if self.suggestedPlayerCountVote(int(playercount),'Best') >= votetolerance:
			return True
		else:
			return False

	def isRecommendedWith(self,playercount,votetolerance=50):
		#Sweeping assumption that we accept 'best' votes if we are looking for 'recommended' votes
		if self.suggestedPlayerCountVote(int(playercount),'Best') >= votetolerance:
			return True
		else:
			if self.suggestedPlayerCountVote(int(playercount),'Recommended') >= votetolerance:
				return True
		return False

#Define classes for the UI elements
class DetailPopup(QDialog, Ui_GameDetail):

	BEST, RECOMMENDED, NOTRECOMMENDED, TOTAL = range(4)

	def __init__(self,bggid,parent=None):
		super(DetailPopup,self).__init__(parent)
		self.ui=Ui_GameDetail()
		self.ui.setupUi(self)
		self.ui.bgName.setText(bgcollection[bggid]["name"])
		self.ui.description.setHtml('<div style="font-size:14pt">'+bgcollection[bggid]["description"]+'</div>')
		imagestring = '_md.'.join(bgcollection[bggid]["image"].rsplit('.',1))
		self.ui.imageDisplay.setHtml('<div style="text-align: center; vertical-align: middle"><img src='+imagestring+'></div>')
		self.ui.closeButton.clicked.connect(self.done)
		self.ui.votingData.clear()
		self.ui.votingData.setSortingEnabled(False)
		#replace headers - clear() deletes them :(
		headers = ["Best", "Recommended", "Not Recommended", "Total"]
		self.ui.votingData.setHorizontalHeaderLabels(headers)
		#fetch voting data and populate table
		#clunky arsed way to get the suggestedplayercount values
		playercountlist = list(bgcollection[bggid]['suggestedplayercount'].keys())
		playercountlist.remove('totalvotes')
		self.ui.votingData.setRowCount(len(playercountlist))
		for row,playercount in enumerate(playercountlist):
			#Best votes column
			item = QTableWidgetItem(str(bgcollection[bggid].suggestedPlayerCountVoteRaw(playercount,'Best')) + " (" + str(bgcollection[bggid].suggestedPlayerCountVote(playercount,'Best'))+ "%)")
			item.setTextAlignment(Qt.AlignCenter|Qt.AlignVCenter)
			self.ui.votingData.setItem(row, self.BEST, item)
			#Recommended votes column
			item = QTableWidgetItem(str(bgcollection[bggid].suggestedPlayerCountVoteRaw(playercount,'Recommended')) + " (" + str(bgcollection[bggid].suggestedPlayerCountVote(playercount,'Recommended'))+ "%)")
			item.setTextAlignment(Qt.AlignCenter|Qt.AlignVCenter)
			self.ui.votingData.setItem(row, self.RECOMMENDED, item)
			#Not Recommended votes column
			item = QTableWidgetItem(str(bgcollection[bggid].suggestedPlayerCountVoteRaw(playercount,'Not Recommended')) + " (" + str(bgcollection[bggid].suggestedPlayerCountVote(playercount,'Not Recommended'))+ "%)")
			item.setTextAlignment(Qt.AlignCenter|Qt.AlignVCenter)
			self.ui.votingData.setItem(row, self.NOTRECOMMENDED, item)
			#Total Votes column
			item = QTableWidgetItem(bgcollection[bggid].suggestedPlayerCountVoteTotal(playercount))
			item.setTextAlignment(Qt.AlignCenter|Qt.AlignVCenter)
			self.ui.votingData.setItem(row, self.TOTAL, item)
		#sort out player count row labels
		playercountliststr = []
		for item in playercountlist:
			#turn them into strings
			playercountliststr.append(str(item))
		self.ui.votingData.setVerticalHeaderLabels(playercountliststr)
		self.ui.votingData.setColumnWidth(self.BEST,100)
		self.ui.votingData.setColumnWidth(self.RECOMMENDED,190)
		self.ui.votingData.setColumnWidth(self.NOTRECOMMENDED,199)
		self.ui.votingData.setColumnWidth(self.TOTAL,110)

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
		self.ui.resetAll.clicked.connect(lambda: self.resetButtonclicked())
		self.playtimebuttonset = set()
		self.playtimebuttonset.add(self.ui.Btn30mins)
		self.playtimebuttonset.add(self.ui.Btn60mins)
		self.playtimebuttonset.add(self.ui.Btn90mins)
		self.playtimebuttonset.add(self.ui.Btn120mins)
		self.playtimebuttonset.add(self.ui.Btn150mins)
		self.playtimebuttonset.add(self.ui.Btn180mins)
		#wire up the list items
		self.ui.mechaniclist.itemClicked.connect(lambda: self.mechanicFilter())
		self.ui.categorylist.itemClicked.connect(lambda: self.categoryFilter())
		#wire the boardgame table up to the details popup
		self.ui.bgcollectionView.itemClicked.connect(lambda: self.showdetails(self.ui.bgcollectionView.item(self.ui.bgcollectionView.currentRow(),self.NAME).data(Qt.UserRole)))
		#and finally link in the admin screen
		self.ui.downloadData.clicked.connect(lambda: self.downloadData())		
		#size/format overrides not easily configurable from QTDesigner
		self.ui.bgcollectionView.verticalScrollBar().setStyleSheet("QScrollBar:vertical { width: 50px; }")
		self.ui.bgcollectionView.horizontalHeader().setMinimumHeight(5)
		self.ui.mechaniclist.verticalScrollBar().setStyleSheet("QScrollBar:vertical { width: 50px; }")
		self.ui.categorylist.verticalScrollBar().setStyleSheet("QScrollBar:vertical { width: 50px; }")
		self.ui.bgcollectionView.setColumnWidth(self.NAME,576)
		self.ui.bgcollectionView.setColumnWidth(self.MINPLAYERS,75)
		self.ui.bgcollectionView.setColumnWidth(self.MAXPLAYERS,75)
		self.ui.bgcollectionView.setColumnWidth(self.PLAYTIME,75)
		self.ui.resetAll.setVisible(False)
		#Initial setup
		self.updateUI()

	def resetButtonclicked(self):
		resetAllFilters()
		self.updateUI()

	def updateUI(self):
		combinefilters()
		#Are we filtering?
		if len(filteredset) == len(allbgids):
			#nope, hide the reset button and turn off all the buttons
			self.ui.resetAll.setVisible(False)
			for button in self.playercountbuttonset:
				button.setChecked(False)
			self.ui.bestButton.setEnabled(False)
			self.ui.recommendedButton.setEnabled(False)
			for i in range(self.ui.mechaniclist.count()):
				       self.ui.mechaniclist.setItemSelected(self.ui.mechaniclist.item(i), False)
			for i in range(self.ui.categorylist.count()):
				       self.ui.categorylist.setItemSelected(self.ui.categorylist.item(i), False)
		else:
			self.ui.resetAll.setVisible(True)
			self.reconfigurebuttons()
		self.populateLists()
		self.populateTable()

	def reconfigurebuttons(self):
		#reconfigures the playercount and playtime buttons to match any selections elsewhere
		#key goal here is that we need to make it impossible to choose a player count that would
		#make a currently selected mechanicm or theme disappear
		#fetch the min and max player count from the current filtered list
		minplayers = 9
		maxplayers = 2
		for bgid in filteredset:
			if bgcollection[bgid]["minplayers"] < minplayers:
				minplayers = bgcollection[bgid]["minplayers"]
			if bgcollection[bgid]["maxplayers"] > maxplayers:
				maxplayers = bgcollection[bgid]["maxplayers"]
		#now to en/disable buttons below minplayers and above maxplayers
		for number in range(2,10):
			if number < minplayers:
				exec('self.ui.Btn'+str(number)+'Player.setDisabled(True)')
			elif number > maxplayers:
				exec('self.ui.Btn'+str(number)+'Player.setDisabled(True)')
			else:
				exec('self.ui.Btn'+str(number)+'Player.setDisabled(False)')

	def populateLists(self):
		#populate mechanic/category lists with values
		#first, remember what we have selected
		selection = []
		for mechanism in self.ui.mechaniclist.selectedItems():
			selection.append(mechanism.text())
		#that is stored, clear and repopulate
		self.ui.mechaniclist.clear()
		for mechanic in mechanics:
			self.ui.mechaniclist.addItem(mechanic)
		self.ui.mechaniclist.sortItems()
		#now reselect previously selected items
		for mechanic in selection:
			for item in self.ui.mechaniclist.findItems(mechanic,Qt.MatchFixedString):
				item.setSelected(True)
		#what feels like uncessary faff to resize rows
		for x in range(0,len(self.ui.mechaniclist)):
			self.ui.mechaniclist.item(x).setSizeHint(QSize(750,30))
		#and do the same for the category list
		selection = []
		for category in self.ui.categorylist.selectedItems():
			selection.append(category.text())
		self.ui.categorylist.clear()
		for category in categories:
			self.ui.categorylist.addItem(category)
		self.ui.categorylist.sortItems()
		for category in selection:
			for item in self.ui.categorylist.findItems(category,Qt.MatchFixedString):
				item.setSelected(True)
		for x in range(0,len(self.ui.categorylist)):
			self.ui.categorylist.item(x).setSizeHint(QSize(750,30))

	
	def populateTable(self):
		#clear and disable sorting
		self.ui.bgcollectionView.clear()
		self.ui.bgcollectionView.setSortingEnabled(False)
		#replace headers - clear() deletes them :(
		headers = ["Name", "Min.\nPlayers", "Max.\nPlayers", "Playing\nTime"]
		self.ui.bgcollectionView.setHorizontalHeaderLabels(headers)
		#get the filtered list length and start populating
		self.ui.bgcollectionView.setRowCount(len(filteredset))
		for row, boardgame in enumerate(filteredset):
			#set row height
			self.ui.bgcollectionView.setRowHeight(row,30)
			#name column
			item = QTableWidgetItem(bgcollection[boardgame]["name"])
			item.setData(Qt.UserRole, bgcollection[boardgame]["ID"])
			self.ui.bgcollectionView.setItem(row, self.NAME, item)
			#minplayers column
			item = QTableWidgetItem(str.rjust(str(bgcollection[boardgame]["minplayers"]),2))
			item.setTextAlignment(Qt.AlignCenter|Qt.AlignVCenter)
			self.ui.bgcollectionView.setItem(row, self.MINPLAYERS, item)
			#maxplayers column
			item = QTableWidgetItem(str.rjust(str(bgcollection[boardgame]["maxplayers"]),2))
			item.setTextAlignment(Qt.AlignCenter|Qt.AlignVCenter)
			self.ui.bgcollectionView.setItem(row, self.MAXPLAYERS, item)
			#playingtime column
			item = QTableWidgetItem(str.rjust(str(bgcollection[boardgame]["maxplaytime"]),3))
			item.setTextAlignment(Qt.AlignCenter|Qt.AlignVCenter)
			self.ui.bgcollectionView.setItem(row, self.PLAYTIME, item)
		#reenable sorting
		self.ui.bgcollectionView.setSortingEnabled(True)
		self.ui.bgcollectionView.horizontalHeader().setSortIndicatorShown(False)
		#TODO: kinda want to keep track of whatever the 'current' sort is
		self.ui.bgcollectionView.sortItems(self.NAME)
		#update the results LCD
		self.ui.lcdResults.display(self.ui.bgcollectionView.rowCount())

	def playerFilter(self,numplayers,button):
		if button.isChecked():
			numplayerfilter(numplayers)
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
			resetplayerfilter()
			resetsuggestedfilter()
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
			suggestedbestplayercountfilter(numplayers)
			self.ui.recommendedButton.setChecked(False)
		else:
			resetsuggestedfilter()
		self.updateUI()

	def recommendedFilter(self,button):
		if button.isChecked():
			#which player count is currently checked
			numplayers = 0
			for playercountbutton in self.playercountbuttonset:
				if playercountbutton.isChecked():
					numplayers = playercountbutton.text()		
			suggestedrecommendedplayercountfilter(numplayers)
			self.ui.bestButton.setChecked(False)
		else:
			resetsuggestedfilter()
		self.updateUI()	
			
	def playtimeFilter(self,playtime,button):
		if button.isChecked():
			playtimefilter(playtime)
			turnoffset = self.playtimebuttonset.difference({button})
			for button in turnoffset:
				button.setChecked(False)
		else:
			resetplaytimefilter()
		self.updateUI()

	def mechanicFilter(self):
		selection = []
		for mechanism in self.ui.mechaniclist.selectedItems():
			selection.append(mechanism.text())
		mechanicfilter(selection)
		self.updateUI()
		
	def categoryFilter(self):
		selection = []
		for category in self.ui.categorylist.selectedItems():
			selection.append(category.text())
		categoryfilter(selection)
		self.updateUI()

	def downloadData(self):
		ret = QMessageBox.information(self, "Download", "Be warned, this locks up the screen for a good 10 mins.  Continue?",QMessageBox.Ok | QMessageBox.Cancel)
		if ret == QMessageBox.Ok:
			downloadCollection(form)
			loadCollection()
			resetAllFilters()
			#need a 'reset ui' function
			self.updateUI()

	def showdetails(self,selectedgameid):
		#display the details dialog, passing in the BGGID of the selected game
		dlg = DetailPopup(selectedgameid)
		dlg.setWindowFlags(form.windowFlags() | QtCore.Qt.FramelessWindowHint)
		dlg.exec_()

#main execution starts here
#Initialisations - globalise bgcollection otherwise I can't modify it in the override loop
global bgcollection
bgcollection = dict()

#Define the DownloadCollection function
#Downloads data from BGG and pickles it to disk for later use by the loadCollection() function
def downloadCollection(parentwindow, username="Darke"):
	#Initialisations
	collection_url=("https://www.boardgamegeek.com/xmlapi2/geeklist/198243")
	#BGG XMLAPI2 URL for boardgame data)
	BGDataURL = "http://www.boardgamegeek.com/xmlapi2/thing?id="
	#temp list to hold the IDs from the collection
	bgcollectionids = []
	#Master dictionary, index by BGGID
	bgcollection = dict()	
	#Firstly, do an initial connection to start the collection cache process
	collectioncaching = 1
	while collectioncaching == 1:
		collection_probe = urlopen(collection_url)
		#check the HTTP return, 202 means we need to delay
		if collection_probe.getcode() == 202:
			#shut down, go to sleep for 30 secs
			collection_probe.close()
			time.sleep(30)
		else:
			collectioncaching = 0
	#Right, press on with fetching the actual data now that BGG have ti generated      
	#Fetch the 'want to play' collection XML, fill the objectiddict with it                
	with urlopen(collection_url) as collection_xml:
		collectiontree = etree.parse(collection_xml)
		collectionroot = collectiontree.getroot()
		#Stuff all those BGGIDs into a temp list
		for each_child in collectionroot:
			#All we get is the ID here, put it in a temporary list
			if (each_child.tag) == 'item':
				bgcollectionids.append(int(each_child.attrib['objectid']))

	#Now we have the IDs we can iterate the BGGame data XML to populate our objects
	#Once for each ID in the downloaded collection
	progress = QProgressDialog("Downloading data...", None, 0, len(bgcollectionids), parentwindow);
	progress.setWindowModality(Qt.WindowModal);
	progress.show()
	i=0
	for each_objectid in bgcollectionids:
		#Fetch the Game Data XML
		i = i+1
		progress.setValue(i)
		#pause, else we get an HTTP 503 due to abuse
		time.sleep(1)
		with urlopen(BGDataURL+str(each_objectid)) as objectxml:
			objecttree = etree.parse(objectxml)
			objectroot = objecttree.getroot()
			#There can be multiple names, but it looks like the primary name is always index 0
			name = objectroot[0].find('name').attrib['value']
			minplayers = int(objectroot[0].find('minplayers').attrib['value'])
			maxplayers = int(objectroot[0].find('maxplayers').attrib['value'])
			minplaytime = int(objectroot[0].find('minplaytime').attrib['value'])
			maxplaytime = int(objectroot[0].find('maxplaytime').attrib['value'])
			description = objectroot[0].find('description').text
			thumbnail = objectroot[0].find('thumbnail').text
			image = 'http:'+objectroot[0].find('image').text
			#Overly elaborate nested loop structure for fishing out the suggested player count data
			suggestedplayercount = dict()
			#Loop through each poll (there are typically 3)
			for each_poll in objectroot[0].findall('poll'):
				#Have we found 'suggested_numplayers?' (as opposed to language dependence or suggested player age)
				if (each_poll.attrib['name'] == 'suggested_numplayers'):
					#Fetch the total unique voters for all player counts
					suggestedplayercount['totalvotes'] = int(each_poll.attrib['totalvotes'])
					#Loop through each sub poll (one for each player count)
					for each_numplayerpoll in each_poll.getchildren():
						#Which numplayers subpoll is this?
						numplayers = each_numplayerpoll.attrib['numplayers']
						#Does it end with a +? Don't bother progressing if it does
						if not numplayers.endswith('+'):
							#The + has gone - we can safely int() this now :)
							numplayers = int(numplayers)
							#Check we are within the min and max player counts - we don't care about votes outside of that
							if (numplayers >= minplayers) and (numplayers <= maxplayers):
								voteresults = dict()
								#For each vote answer (best, recommended, not recommended) store the name and the vote count)
								for each_voteanswer in each_numplayerpoll.getchildren():
									voteresults[each_voteanswer.attrib['value']] = int(each_voteanswer.attrib['numvotes'])
								#Put the results of this subpoll into the dictionary, keyed by the number of players
								suggestedplayercount[numplayers] = voteresults		
			#Parse categories and mechanics
			categories = list()
			mechanics = list()
			for each_link in objectroot[0].findall('link'):
				#is this a category?
				if (each_link.attrib['type'] == 'boardgamecategory'):
					categories.append(each_link.attrib['value'])
				#if it's not a category - is it a mechanic?
				elif (each_link.attrib['type'] == 'boardgamemechanic'):
					mechanics.append(each_link.attrib['value'])
			#Create the boardgame object, shove it in the collection dict
			bgcollection[each_objectid] = boardgamedict(each_objectid,name,minplayers,maxplayers,minplaytime,maxplaytime,description,thumbnail,image,suggestedplayercount,categories,mechanics)

	#Pickle the lot to disk for later use
	try:
		with open('collection.pickle', 'wb') as bgcollectionf:
			pickle.dump(bgcollection,bgcollectionf)
	except IOError as err:
		print('File error: ' + str(err))
	except pickle.PickleError as perr:
		print('Pickling error: ' + str(perr))

def loadCollection():
	global bgcollection
	#Load collection from disk
	try:
		with open('collection.pickle', 'rb') as bgcollectionf:
			bgcollection = pickle.load(bgcollectionf)
	except IOError as err:
		print('File error: ' + str(err))
	except pickle.PickleError as perr:
		print('Pickling error: ' + str(perr))
		
	#Load local overrides
	try:
		with open('LocalOverrides.txt', 'r') as overridesf:
			for each_line in overridesf:
				#ignore comment lines
				if not each_line.startswith('#'):
					(bgid,key,value) = each_line.split(',')
					try:
						bgcollection[int(bgid)][key] = int(value)
					except ValueError:
						bgcollection[int(bgid)][key] = value
	except IOError as err:
		print('File error: ' + str(err))

#initial load
if os.name == 'nt':
    #Windows
    os.chdir('C:\Dropbox\Coding\GameSelector')
else:
    #other
    os.chdir('/home/pi/GameSelector')
loadCollection()
#Get all known mechanics and categories into sets
allmechanics = set()
allcategories = set()
for BGID in bgcollection.keys():
	for mechanic in bgcollection[BGID]['mechanics']:
		allmechanics.add(mechanic)
	for category in bgcollection[BGID]['categories']:
		allcategories.add(category)
#Initialise filters - create them all as 'complete set' to start with
allbgids = set(bgcollection.keys())
filteredset = allbgids
numplayerset = allbgids
playtimeset = allbgids
suggestedbestset = allbgids
mechanicset = allbgids
categoryset = allbgids
#filters for the selection lists
mechanics = allmechanics
categories = allcategories	

def resetAllFilters():
	resetplayerfilter()
	resetplaytimefilter()
	resetsuggestedfilter()
	resetmechanicfilter()
	resetcategoryfilter()
	combinefilters()
	
def resetplayerfilter():
	global numplayerset
	numplayerset = allbgids
	
def numplayerfilter(numplayers):
	global numplayerset
	numplayerset = set([BGID for BGID in bgcollection.keys() if bgcollection[BGID]['minplayers'] <= numplayers <= bgcollection[BGID]['maxplayers']])

def resetplaytimefilter():
	global playtimeset
	playtimeset = allbgids

def playtimefilter(playtime):
	global playtimeset
	playtimeset = set([BGID for BGID in bgcollection.keys() if bgcollection[BGID]['maxplaytime'] <= playtime])

def resetsuggestedfilter():
	global suggestedbestset
	suggestedbestset = allbgids
	
def suggestedbestplayercountfilter(numplayers,votetolerance=50):
	global suggestedbestset
	suggestedbestset = set([BGID for BGID in bgcollection.keys() if bgcollection[BGID].isBestWith(numplayers,votetolerance)])

def suggestedrecommendedplayercountfilter(numplayers,votetolerance=50):
	global suggestedbestset
	suggestedbestset = set([BGID for BGID in bgcollection.keys() if bgcollection[BGID].isRecommendedWith(numplayers,votetolerance)])                

def resetmechanicfilter():
	global mechanicset
	mechanicset = allbgids

def mechanicfilter(mechaniclist):
	global mechanicset
	bgidset = set()
	for BGID in allbgids:
		#Counter to check matching number of mechanics
		mechcount = 0
		for mechanic in mechaniclist:
			if mechanic in bgcollection[BGID]['mechanics']:
				mechcount += 1
		#number of matches = number of passed mechanics?
		if mechcount == len(mechaniclist):
			bgidset.add(BGID)
	mechanicset = bgidset

def resetcategoryfilter():
	global categoryset
	categoryset = allbgids

def categoryfilter(categorylist):
	global categoryset
	bgidset = set()
	for BGID in bgcollection.keys():
		#Counter to check matching number of categories
		catcount = 0
		for category in categorylist:
			if category in bgcollection[BGID]['categories']:
				catcount += 1
		#number of matches = number of passed categories?
		if catcount == len(categorylist):
			bgidset.add(BGID)
	categoryset = bgidset

def combinefilters():
	global filteredset,numplayerset,playtimeset,suggestedbestset,mechanicset,categoryset,mechanics,categories
	filteredset = set.intersection(numplayerset,playtimeset,suggestedbestset,mechanicset,categoryset)
	#strip down the mechanics list to match the newly filtered set of games
	#first, check if we're filtering at all
	if len(filteredset) == len(allbgids):
		#nope, reset them to 'all'
		mechanics = allmechanics
		categories = allcategories
	else:
		mechanics = set()
		categories = set()
		for BGID in filteredset:
			for mechanic in bgcollection[BGID]['mechanics']:
				mechanics.add(mechanic)
			for category in bgcollection[BGID]['categories']:
				categories.add(category)
				
if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = MainForm()
	#Dis/Enable next line for frameless
	#form.setWindowFlags(form.windowFlags() | QtCore.Qt.FramelessWindowHint)
	form.showMaximized()
	sys.exit(app.exec_())
