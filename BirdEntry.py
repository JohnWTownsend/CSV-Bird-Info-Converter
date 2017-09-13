from Functions import *
class BirdEntry(object): # just in case cName, count, state, county, date

	def __init__(self, cName, count, county, loc, date, breed, scomm):
		self.cName = self.getCName(cName)
		self.count = int(count) if isInt(count) else 0
		self.county = county
		self.loc = commaCheck(loc)
		self.date = date
		self.breed = commaCheck(breed)
		self.scomm = commaCheck(scomm)

	def getCName(self, cName):
		if cName == "Orchard Orioloe":
			returnCName = "Orchard Oriole"
		elif cName == "White-winged Junco":
			returnCName = "Dark-eyed Junco"
		elif cName == "LeConte's Sparrow":
			returnCName = "Le Conte's Sparrow"
		elif cName == "McGillivray's Warlber":
			returnCName = "MacGillivray's Warbler"
		elif cName == "Northern Flicker (Yellow-shafted)" or cName == "Northern Flicker (Red-shafted)":
			returnCName = "Northern Flicker"
		elif cName == "Rock Pigeon (Feral Pigeon)":
			returnCName = "RockPigeon"
		elif cName == "Yellow-rumped Warbler (Myrtle)":
			returnCName = "Yellow-rumped Warbler"
		elif cName == "Red-tailed hawk (Harlan’s)":
			returnCName = "Red-tailed Hawk"
		elif cName == "Dark-eyed Junco (Slate-colored)":
			returnCName = "Dark-eyed Junco"
		else:	
			returnCName = cName
		return returnCName


