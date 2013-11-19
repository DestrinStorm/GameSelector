#Imports
import pickle
#Import BGGData class
import sys
from bggdata import *

#Initialisations - globalise bgcollection otherwise I can't modify it in the override loop
global bgcollection
bgcollection = dict()

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
	playtimeset = set([BGID for BGID in bgcollection.keys() if bgcollection[BGID]['playingtime'] <= playtime])

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
