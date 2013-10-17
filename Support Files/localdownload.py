"""This module is designed to connect and download the 'want to play' list for
a specific user on boardgamegeek.com, format each boardgame into it's own object
and then output that data to the file system for later use"""

#Imports
from urllib.request import urlopen
import xml.etree.ElementTree as etree
import pickle

#Define the boardgame class
#Extend dictionary and assign the appropriate data to preset key names
class boardgamedict(dict):
	def __init__(self, ID, name, minplayers, maxplayers, playingtime, description='', thumbnail='', image='', suggestedplayercount=dict()):
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

#Initialisations
#BGG XMLAPI2 URL for the collection to download
collection_url = "http://www.boardgamegeek.com/xmlapi2/collection?username=Darke&wanttoplay=1"
#BGG XMLAPI2 URL for boardgame data)
BGDataURL = "C:\Dropbox\Coding\GameSelector\\"
#temp list to hold the IDs from the collection
bgcollectionids = []
#Master dictionary, index by BGGID
bgcollection = dict()

#Fetch the 'want to play' collection XML, fill the objectiddict with it
"""with urlopen(collection_url) as collection_xml:
	collectiontree = etree.parse(collection_xml)
	collectionroot = collectiontree.getroot()
	#Instantiate a boardgame object for each entry
	for each_child in collectionroot:
		#All we get is the ID here, put it in a temporary list
		bgcollectionids.append(int(each_child.attrib['objectid']))"""
bgcollectionids.append(1)

#Now we have the IDs we can iterate the BGGame data XML to populate our objects
#Once for each ID in the downloaded collection 
for each_objectid in bgcollectionids:
	#Fetch the Game Data XML
	with open(BGDataURL+str(each_objectid)+".xml") as objectxml:
		objecttree = etree.parse(objectxml)
		objectroot = objecttree.getroot()
		#name is funky - might need to locate the 'primaryname' rather than index 0
		name = objectroot[0].find('name').attrib['value']
		minplayers = int(objectroot[0].find('minplayers').attrib['value'])
		maxplayers = int(objectroot[0].find('maxplayers').attrib['value'])
		playingtime = int(objectroot[0].find('playingtime').attrib['value'])
		description = objectroot[0].find('description').text
		thumbnail = objectroot[0].find('thumbnail').text
		image = objectroot[0].find('image').text
		#Overly elaborate nested loop structure for fishing out the suggested player count data
		suggestedplayercount = dict()
		for each_poll in objectroot[0].findall('poll'):
			if (each_poll.attrib['name'] == 'suggested_numplayers'):
				for each_numplayerpoll in each_poll.getchildren():
					numplayers = each_numplayerpoll.attrib['numplayers']
					if not numplayers.endswith('+'):
						numplayers = int(numplayers)
						if (numplayers >= minplayers) and (numplayers <= maxplayers):
							voteresults = dict()
							for each_voteanswer in each_numplayerpoll.getchildren():
								voteresults[each_voteanswer.attrib['value']] = int(each_voteanswer.attrib['numvotes'])
							suggestedplayercount[numplayers] = voteresults		
		#Create an object, shove it in the collection dict
		bgcollection[each_objectid] = boardgamedict(each_objectid,name,minplayers,maxplayers,playingtime,description,thumbnail,image,suggestedplayercount)
"""
#Pickle the lot to disk for later use
try:
	with open('C:\Dropbox\Coding\GameSelector\collection.pickle', 'wb') as bgcollectionf:
		pickle.dump(bgcollection,bgcollectionf)
except IOError as err:
	print('File error: ' + str(err))
except pickle.PickleError as perr:
	print('Pickling error: ' + str(perr))
"""
