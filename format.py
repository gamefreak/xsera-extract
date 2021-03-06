#! /usr/bin/python

import sys

def object(obj, level = 0):
	print "{"
	level += 1
	
	if type(obj) == dict:
		iter = obj.iteritems()
	else:
		iter = enumerate(obj)
	
	for key, val in iter:
		if type(key) == str:
			key = "".join(key.title().split(" "))
			key = key[0].lower() + key[1:]
			print "\t" * level + key + ' =',
		else:
			print "\t" * level + '[' + str(key) + '] =',
		if type(val) == dict:
			object(val, level)
		elif type(val) == int:
			if key == "hex":#Special Case
				print hex(val) + ";"
			else:
				print str(val) + ";"
		elif type(val) == float:
			print str(val) + ";"
		elif type(val) == bool:
			print str(val).lower()+";"
		elif type(val) == str:
			print '"' + str(val) + '";'
		elif type(val) == list:
			object(val, level)
		else:
			print "nil;"
	level -= 1
	print "\t" * level + "};"
