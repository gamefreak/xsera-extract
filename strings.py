#! /usr/bin/python

from struct import unpack
from glob import glob

db = {}

def readStrings(fromFile):
	strings = {}
	count = unpack(">h", fromFile.read(2))[0]
	for i in range(0, count-1):
		len = unpack("B", fromFile.read(1))[0]
		s = unpack(str(len) + "s", fromFile.read(len))[0]
		s = s.replace("\\", "\\\\").replace("\"", "\\\"").replace("\r", "\\r")
		s = s.replace("\xD5", "'")
		strings[i] = s
	return strings

def get(file, id = None):
	if id == None:
		try:
			fd = open("./data/TEXT/r."+str(file))
			text = fd.read()
			fd.close()
		except IOError:
			text = ""
		return text.replace("\"", "\\\"").replace("\r", "\\n")
	elif id is True:
		return db[str(file)]
	else:
		try:
			return db[str(file)][id]
		except:
			return ""

for fileName in glob("./data/STR#/r.*"):
	num = fileName.split('.')[-1]
	file = open(fileName)
	db[num] = readStrings(file)
	file.close()
