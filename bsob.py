#! /usr/bin/python

import struct
import decode
import strings

attributes = [
"can turn", "can be engaged", "has direction goal", "is remote",
"is human controlled", "is beam", "does bounce", "is self animated",
"shape from direction", "is player ship", "can be destination", "can engage",
"can evade", "can accept messages", "can accept build", "can accept destination",
"auto target", "animation cycle", "can collide", "can be hit",
"is destination", "hide effect", "release energy on death", "hated",
"occupies space", "static destination", "can be evaded", "neutral death",
"is guided", "appear on radar", "", "on auto pilot",
]

buildFlags = [
"uncaptured base exists", "sufficient escort exists", "this base needs protection", "friend up trend",
"friend down trend", "foe up trend", "foe down trend", "matching foe exists",
"", "", "", "",
"", "", "", "",
"", "", "", "",
"", "", "only engaged by", "can only engage",
"engage key 1", "engage key 2", "engage key 3", "engage key 4",
"level key 1", "level key 2", "level key 3", "level key 4",
]

orderFlags = [
"stronger than target", "target is base", "target is not base", "target is local",
"target is remote", "only escort not base", "target is friend", "target is foe",
"", "", "", "",
"", "", "", "",
"", "", "hard matching friend", "hard matching foe",
"hard friendly escort only", "hard no friendly escort", "hard target is remote", "hard target is local",
"hard target is foe", "hard target is friend", "hard target is not base", "hard target is base",
"order key 1", "order key 2", "order key 3", "order key 4",
		]

deviceUses = [
"transportation", "attacking", "defence", "",
"", "", "", "",
"", "", "", "",
"", "", "", "",
"", "", "", "",
"", "", "", "",
"", "", "", "",
"", "", "", "",
]

length = 318
format = ">Iiii ii iiI ii ii iii ii i hhiBx ii iii iii 6i6i6i iii i 12i 32s II iI BBBB h 10x"

def parse(file, id = None):
	data = file.read(length)
	values = struct.unpack(format, data)

	object = {}

	object["attributes"] = decode.bitfield(values[0], attributes)
	object["class"] = values[1]
	object["race"] = values[2]
	object["price"] = values[3]

	object["offence"] = decode.fixed(values[4])
	object["escort rank"] = values[5]#aka target, aka destination class
	
	object["max velocity"] = decode.fixed(values[6])
	object["warp speed"] = decode.fixed(values[7])
	object["warp out distance"] = values[8]

	object["inital velocity"] = decode.fixed(values[9])
	object["inital velocity range"] = decode.fixed(values[10])

	object["mass"] = decode.fixed(values[11])
	object["thrust"] = decode.fixed(values[12])

	object["health"] = values[13]
	object["damage"] = values[14]
	object["energy"] = values[15]

	object["initial age"] = values[16]
	object["initial age range"] = values[17] #add occuping force hack

	object["scale"] = values[18] #was natural scale

	object["layer"] = values[19]
	object["sprite id"] = values[20]
	object["icon size"] = values[21]
	object["shield color"] = values[22]
	
	#**** compiler alignment

	object["initial direction"] = values[23]
	object["initial direction range"] = values[24]

	object["weapons"] = {
			"pulse": {
				"id": values[25],
				"count": values[28],
				"positions": {},
				},
			"beam": {
				"id": values[26],
				"count": values[29],
				"positions": {},
				},
			"special": {
				"id": values[27],
				"count": values[30],
				"positions": {},
				},
			}
	ct = 31
	for weap in ["pulse", "beam", "special"]:
		for idx in range(0, object["weapons"][weap]["count"]):
			object["weapons"][weap]["positions"][idx + 1] = {
						"y": decode.fixed(values[ct+2*idx]),
						"x": decode.fixed(values[ct+2*idx+1]),
					}
		ct += 6
	
	object["friend defecit"] = decode.fixed(values[49])
	object["danger threshold"] = decode.fixed(values[50])

	object["special direction"] = values[51] #unused?

	object["arrive action distance"] = values[52]

	object["actions"] = {
			"destroy": {
				"id": values[53],
				"count": values[54] & 0x7fffffff,
				"dont die on death": bool(values[54] & 0x80000000),
				},
			"expire": {
				"id": values[55],
				"count": values[56],
				},
			"create": {
				"id": values[57],
				"count": values[58],
				},
			"collide": {
				"id": values[59],
				"count": values[60],
				},
			"activate": {
				"id": values[61],
				"count": values[62] & 0x0000ffff,
				"interval": (values[62] & 0xff000000) >> 24,
				"interval range": (values[62] & 0x00ff0000) >> 16,
				},
			"arrive": {
				"id": values[63],
				"count": values[64],
				},
			}
	
	if object["attributes"]["shape from direction"] == True:
		frame = struct.unpack(">iiii 16x", values[65])
		object["rotation"] = {
				"offset": frame[0],
				"resolution": frame[1],
				"turn rate": decode.fixed(frame[2]),
				"turn acceleration": decode.fixed(frame[3]),
				}
	elif object["attributes"]["is self animated"] == True:
		frame = struct.unpack(">8i", values[65])
		object["animation"] = {
			"first shape": frame[0],
			"last shape": frame[1],
			"direction": frame[2],
			"direction range": frame[3],
			"speed": frame[4],
			"speed range": frame[5],
			"shape": frame[6],
			"shape range": frame[7],
			}
	elif object["attributes"]["is beam"] == True:
		frame = struct.unpack(">BBii", values[65])
		object
		if frame[1] == 0:
			object["beam"] = {
				"hex": 0x0, #000
				"type": "kinetic",
				"mode": Null,
				}
		elif frame[1] == 1:
			object["beam"] = {
				"hex": 0x2, #010
				"type": "static",
				"mode": "direct",
				}
		elif frame[1] == 2:
			object["beam"] = {
				"hex": 0x3, #011
				"type": "static",
				"mode": "relative",
				}
		elif frame[1] == 3:
			object["beam"] = {
				"hex": 0x4, #100
				"type": "bolt",
				"mode": "direct",
				}
		elif frame[1] == 4:
			object["beam"] = {
				"hex": 0x5, #101
				"type": "bolt",
				"mode": "relatice",
				}

			object["beam"]["color"] = frame[0]
			object["beam"]["accuracy"] = frame[2]
			object["beam"]["range"] = frame[3]
	else: #device
		frame = struct.unpack(">Iiiiiii 4x", values[65])
		object["device"] = {
			"uses": decode.bitfield(frame[0], deviceUses),
			"energy cost": frame[1],
			"reload": frame[2],
			"ammo": frame[3],
			"range": frame[4],
			"inverse speed": frame[5],
			"restock cost": frame[6],
			}
	object["build flage"] = decode.bitfield(values[66], buildFlags)
	object["order flags"] = decode.bitfield(values[67], orderFlags)
	
	object["build ratio"] = decode.fixed(values[68])
	object["build time"] = values[69]

	object["skill num"] = values[70]
	object["skill den"] = values[71]
	object["skill num adj"] = values[72]
	object["skill den adj"] = values[73]
	
	object["portrait id"] = values[74]
	
	if id != None:
		object["name"] = strings.get(5000, id)
		object["short name"] = strings.get(5001, id)
		object["notes"] = strings.get(5002, id)
		object["static name"] = strings.get(5003, id)
	return object

