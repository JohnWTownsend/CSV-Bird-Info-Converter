from datetime import datetime

def isInt(val):
	try:
		int(val)
		return True
	except:
		return False

def isDate(val):
	try:
		datetime(val)
		return True
	except:
		return False

def commaCheck(checkString):
	new = ""
	for char in range(len(checkString)):
		if checkString[char] == ",":
			new += ";"
		else:
			new += checkString[char]
	return "".join(new)	
def IsValidBird(bird):
	if bird.cName != "Snow/Ross’s Goose":
		return True
	return False

def IsRowInSD(row):
	if row[5] == "US-SD":
		return True
	return False
