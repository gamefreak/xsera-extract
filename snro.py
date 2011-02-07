#! /usr/bin/python

from struct import unpack
import strings
import decode

size = 124

format = "> hh 4h4xih2x 4h4xih2x 4h4xih2x 4h4xih2x 11h bb 4h ihh"

def parse(file, id = None):
	data = file.read(size)
	try:
		values = unpack(format, data)
	except:
		return None
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
		player["name"] = strings.get(values[2+6*i+2], values[2+6*i+3]- 1)
		#player["admiral number"] = values[2+8*i+4] #unused it seems
		player["earning power"] = decode.fixed(values[2+6*i+4])
		player["net race flags"] = values[2+6*i+5]
		object["players"][i+1] = player
	
	if values[26] > 0:
		object["score string"] = strings.get(values[26], True)
	else:
		object["score string"] = []
	object["initial objects"] = {
			"first": values[27],
			"count": values[29],
			}
	
	object["prologue"] = strings.get(values[28])
	object["epilogue"] = strings.get(values[32])

	object["song id"] = values[30]

	object["conditions"] = {
			"first": values[31],
			"count": values[33],
			}

	object["starmap"] = {
			"x": values[34],
			"y": values[36],
			}

	object["angle"] = values[37]

	object["briefing"] = {
			"first": values[35],
			"count": values[38],
			}

	object["par"] = {
			"time": values[39],
			"kills": values[41],
			"ratio": decode.fixed(values[43]),
			"losses": values[44],
			}

	if values[40] > -1:
		object["movie"] = strings.get(4500, values[40])
	else:
		object["movie"] = None

	object["id"] = values[42]
	object["name"] = strings.get(4600, values[42]-1)

	object["start time"] = 0x7fff & values[45]
	object["is training"] = (0x8000 & values[45]) == True
	return object
