# -*- coding: utf-8 -*-

from Functions import *
class BirdEntry(object):

    def __init__(self, commonName, count, county, loc, date, breed, scomm):
        self.commonName = getCommonName(commonName)
        self.count = int(count) if isInt(count) else 0
        self.county = county
        self.loc = commaCheck(loc)
        self.date = date
        self.breed = getBreed(breed)
        self.scomm = commaCheck(scomm)