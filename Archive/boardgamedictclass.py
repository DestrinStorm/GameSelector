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

	def suggestedplayercountvote(self,playercount,votetype='Best'):
		if playercount in self['suggestedplayercount'].keys():
			bestvotes = self['suggestedplayercount'][playercount][votetype]
			totalvotes = self['suggestedplayercount']['totalvotes']
			percentage = (bestvotes / totalvotes) * 100
			return round(percentage)
		else:
			return 0

	def isBestWith(self,playercount):
		if self.suggestedplayercountvote(playercount,'Best') >= 50:
			return True
		else:
			return False
