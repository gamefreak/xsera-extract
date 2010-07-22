#! /usr/bin/python

from struct import unpack
from glob import glob

db = {}

def readStrings(fromFile):
	strings = []
	count = unpack(">h", fromFile.read(2))[0]
	for i in range(1, count):
		len = unpack("B", fromFile.read(1))[0]
		s = unpack(str(len) + "s", fromFile.read(len))[0]
		strings.append(s)
	return strings

def get(file, id):
	return db[str(file)][id]

for fileName in glob("./data/STR#/r.*"):
	num = fileName.split('.')[-1]
	file = open(fileName)
	db[num] = readStrings(file)
	file.close()
