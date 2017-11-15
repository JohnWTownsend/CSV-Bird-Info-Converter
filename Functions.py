# -*- coding: utf-8 -*-
from dateutil.parser import *
from datetime import *

commonNameDict = {}

def populateCommonNameDict(file):
    for i in file:
        i = i.split(":")
        commonNameDict[i[0]] = i[1].rstrip()

def getCommonName(bird):
    if commonNameDict.has_key(bird):
        return commonNameDict[bird]
    else:
        return bird

def getBreed(breed):
    abbr = ""
    breedWords = breed.split(" ")
    if breed:
        abbr = breedWords[0]
    if abbr in { "CF", "CN", "DD", "FL", "FS", "FY", "NB", "NE", "NY", "ON", "PE", "PY", "UN" }:
        return abbr
    else:
        return ""

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
    if bird.commonName != "Snow/Ross’s Goose":
        return True
    return False

def IsRowInSD(row):
    try:   
        if row[5] == "US-SD":
            return True
    except:
        return False

def RemoveOutOfDateBirds(birdArray, start, end):
    removeArr = []
    for bird in birdArray:
        birdDate = parse(bird.date)
        print str(start) + " < " + str(bird.date) + " < " + str(end)
        if start > birdDate or birdDate > end:
            print "removing"
            removeArr.append(bird)
            
    for bird in removeArr:
        birdArray.remove(bird)
            
