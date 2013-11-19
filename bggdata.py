#Imports - core
from urllib.request import urlopen
import xml.etree.ElementTree as etree
import pickle

#Define the boardgame class
#Extend dictionary and assign the appropriate data to preset key names
class boardgamedict(dict):
	def __init__(self, ID, name, minplayers, maxplayers, playingtime, description='', thumbnail='', image='', suggestedplayercount=dict(),categories=list(),mechanics=list()):
		dict.__init__({})
		self["ID"] = int(ID)
		self["name"] = name
		self["minplayers"] = int(minplayers)
		self["maxplayers"] = int(maxplayers)
		self["playingtime"] = int(playingtime)
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
			totalvotes = self['suggestedplayercount']['totalvotes']
			return str(bestvotes) + " / " + str(totalvotes)
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

#Define the DownloadCollection function
def downloadCollection(username="Darke"):
	#Initialisations
	collection_url=("http://www.boardgamegeek.com/xmlapi2/collection?username="+username+"&wanttoplay=1")
	#BGG XMLAPI2 URL for boardgame data)
	BGDataURL = "http://www.boardgamegeek.com/xmlapi2/thing?id="
	#temp list to hold the IDs from the collection
	bgcollectionids = []
	#Master dictionary, index by BGGID
	bgcollection = dict()

	#Fetch the 'want to play' collection XML, fill the objectiddict with it
	with urlopen(collection_url) as collection_xml:
		collectiontree = etree.parse(collection_xml)
		collectionroot = collectiontree.getroot()
		#Stuff all those BGGIDs into a temp list
		for each_child in collectionroot:
			#All we get is the ID here, put it in a temporary list
			bgcollectionids.append(int(each_child.attrib['objectid']))

	#Now we have the IDs we can iterate the BGGame data XML to populate our objects
	#Once for each ID in the downloaded collection 
	for each_objectid in bgcollectionids:
		#Fetch the Game Data XML
		with urlopen(BGDataURL+str(each_objectid)) as objectxml:
			objecttree = etree.parse(objectxml)
			objectroot = objecttree.getroot()
			#There can be multiple names, but it looks lime the primary name is always index 0
			name = objectroot[0].find('name').attrib['value']
			minplayers = int(objectroot[0].find('minplayers').attrib['value'])
			maxplayers = int(objectroot[0].find('maxplayers').attrib['value'])
			playingtime = int(objectroot[0].find('playingtime').attrib['value'])
			description = objectroot[0].find('description').text
			thumbnail = objectroot[0].find('thumbnail').text
			image = objectroot[0].find('image').text
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
			bgcollection[each_objectid] = boardgamedict(each_objectid,name,minplayers,maxplayers,playingtime,description,thumbnail,image,suggestedplayercount,categories,mechanics)

	#Pickle the lot to disk for later use
	try:
		with open('collection.pickle', 'wb') as bgcollectionf:
			pickle.dump(bgcollection,bgcollectionf)
	except IOError as err:
		print('File error: ' + str(err))
	except pickle.PickleError as perr:
		print('Pickling error: ' + str(perr))
