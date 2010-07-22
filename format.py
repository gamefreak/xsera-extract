#! /usr/bin/python

import sys

def write(*arguments):
	for arg in arguments: sys.stdout.write(str(arg))

def line(depth, key, value):
	pass

def object(obj, level = 0):
	print "{"
	level += 1
	for key, val in obj.iteritems():
		if type(key) == str:
			key = "".join(key.title().split(" "))
			key = key[0].lower() + key[1:]
			print "\t" * level + '["' + key + '"] =',
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
		else:
			print "nil;"
	level -= 1
	print "\t" * level + "};"
