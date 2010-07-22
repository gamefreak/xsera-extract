#! /usr/bin/python

from struct import unpack
import decode
import strings

length = 14
format = ">iB x Ii"

def parse(file, id = None):
	data = file.read(length)
	values = unpack(format, data)
	
	object = {}
	
	object["id"] = values[0]
	#apparent color
	#illegal colors
	object["advantage"] = decode.fixed(values[3])

	object["singular"] = strings.get(4201, 4*id + 0)
	object["plural"] = strings.get(4201, 4*id + 1)
	object["military"] = strings.get(4201, 4*id + 2)
	object["home world"] = strings.get(4201, 4*id + 3)
	return object
