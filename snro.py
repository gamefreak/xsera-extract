#! /usr/bin/python

from struct import unpack
import strings
import decode

size = 124

format = "> hh 4h4xih2x 4h4xih2x 4h4xih2x 4h4xih2x 15h 10x"

def parse(file, id = None):
	data = file.read(size)
	values = unpack(format, data)
	object = {}
	
	object["net race flags"] = values[0]
	object["player num"] = values[1]
	
	object["players"] = {}
	for i in range(0, object["player num"]):
		player = {}
		type = values[2+6*i+0]
		if type == 0:
			player["type"] = "single"
		elif type == 1:
			player["type"] = "net"
		elif type == 2:
			player["type"] = "cpu"

		player["race"] = values[2+6*i+1]
		player["name"] = strings.get(values[2+6*i+2], values[2+6*i+3])
		#player["admiral number"] = values[2+8*i+4] #unused it seems
		player["earning power"] = decode.fixed(values[2+6*i+4])
		player["net race flags"] = values[2+6*i+5]
		object["players"][i+1] = player
	
	object["score string"] = strings.get(values[26], True)
	object["initial objects"] = {
			"first": values[27],
			"count": values[29],
			}
	
	object["prologue id"] = values[28],
	object["epilogue id"] = values[32],

	object["song id"] = values[30]

	object["conditions"] = {
			"first": values[31],
			"count": values[33],
			}

	object["starmap"] = {
			"y": values[34],
			"x": values[36],
			}

	object["briefing"] = {
			"first": values[35],
			"count": values[37],
			}

	object["par"] = {
			"time": values[38],
			"kills": values[40],
			}

	if values[39] > -1:
		object["movie"] = strings.get(4500, values[39]-1)
	else:
		object["movie"] = None
	#object["name"] = strings.get(4600, values[41]-1)
	return object
