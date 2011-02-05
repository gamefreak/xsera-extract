#! /usr/bin/python

from struct import unpack
import strings

length = 24

format = "> b x 8s 2i 3h"


def parse(file, id):
	data = file.read(length)
	try:
		values = unpack(format, data)
	except:
		return None

	object = {}
	
	kind = values[0]
	if kind == 0:
		object["kind"] = "no point"
	elif kind == 1:
		object["kind"] = "object"
		sub = unpack("> i ?xxx", values[1])
		object["object id"] = sub[0]
		object["visible"] = sub[1]
	elif kind == 2:
		object["kind"] = "absolute"
	else:
		object["kind"] = "freestanding"
	
	object["range"] = {
			"y": values[2],
			"x": values[3],
		}

	object["title"] = strings.get(values[4], values[5]-1)
	object["content"] = strings.get(values[6])
	return object
