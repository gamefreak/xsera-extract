#! /usr/bin/python

from struct import unpack
import decode

size = 48
format = ">b ? IIhihh 4x 24s"

def parse(file, id = None):
	data = file.read(size)
	values = unpack(format, data)
	
	object = {}
	object["reflexive"] = values[1]
	object["inclusive filter"] = values[2]
	object["exclusive filter"] = values[3]
	object["owner"] = values[4]
	object["delay"] = values[5]

	object["subject override"] = values[6]
	object["direct override"] = values[7]
	
	type = values[0]
	if type == 0:
		object["type"] = "none"
	elif type == 1:
		object["type"] = "create object"
		sub = unpack(">iii??i 6x", values[8])
		object["base type"] = sub[0]
		object["min"] = sub[1]
		object["range"] = sub[2]
		object["velocity relative"] = sub[3]
		object["direction relative"] = sub[4]
		object["distance range"] = sub[5]
	elif type == 2:
		object["type"] = "play sound"
		sub = unpack(">b i?iiii 2x", values[8])
		object["priority"] = sub[0]
		object["persistence"] = sub[1]
		object["is absolute"] = sub[2]
		object["volume"] = sub[3]
		object["volume range"] = sub[4]
		object["sound id"] = sub[5]
		object["sound range"] = sub[6]
	elif type == 3:
		stype, relative, min, range = unpack("> B?ii 14x", values[8])
		if stype == 0:
			"damage",
		elif stype == 1:
			"velocity",
		elif stype == 2:
			"current thrust",
		elif stype == 3:
			"thrust",
		elif stype == 4:
			"max velocity",
		elif stype == 5:
			"turn rate",
		elif stype == 6:
			"location",
		elif stype == 7:
			"scale",
		elif stype == 8:
			"pulse weapon",
		elif stype == 9:
			"beam weapon",
		elif stype == 10:
			"special weapon",
		elif stype == 11:
			"energy",
		elif stype == 12:
			"owner",
		elif stype == 13:
			"hidden",
		elif stype == 14:
			"cloak",
		elif stype == 15:
			"offline",
		elif stype == 16:
			"current turn rate",
		elif stype == 17:
			"base type",
		elif stype == 18:
			"active condition",
		elif stype == 19:
			"occupation",
		elif stype == 20:
			"absolute cash",
		elif stype == 21:
			"age",
		elif stype == 22:
			"absolute location",
	elif type == 4:
		object["type"] = "make sparks"
		sub = unpack(">ii i B 11x", values[8])
		object["count"] = sub[0]
		object["veloctiy"] = sub[1]
		object["velocity range"] = decode.fixed(sub[2])
		object["color"] = sub[3]
	elif type == 5:
		object["type"] = "release energy"
		sub = unpack(">i 20x", values[8])
		object["percent"] = decode.fixed(sub[0])
	elif type == 6:
		object["type"] = "land at"
		sub = unpack(">i 20x", values[8])
		object["speed"] = sub[0]
	elif type == 7:
		object["type"] = "enter warp"
		sub = unpack(">i 20x", values[8])
		object["warp speed"] = sub[0]
	elif type == 8:
		object["type"] = "display message"
		sub = unpack(">hh 20x", values[8])
		object["id"] = sub[0]
		object["page"] = sub[1]
	elif type == 9:
		object["type"] = "change score"
		sub = unpack("> iii 12x", values[8])
		object["plsyer"] = sub[0]
		object["score"] = sub[1]
		object["amount"] = sub[2]
	elif type == 10:
		object["type"] = "declare winner"
		sub = unpack("> iii 12x", values[8])
		object["player"] = sub[0]
		object["next level"] = sub[1]
		object["text"] = sub[2]
	elif type == 11:
		object["type"] = "die"
		sub = unpack("> b 23x", values[8])[0]
		if sub == 0:
			object["how"] = "plain"
		elif sub == 1:
			object["how"] = "expire"
		elif sub == 2:
			object["how"] = "destroy"
	elif type == 12:
		pass
	elif type == 13:
		pass
	elif type == 14:
		pass
	elif type == 15:
		pass
	elif type == 16:
		object["type"] = "color flash"
		sub = unpack("> i BB", values[8])
		object["duration"] = sub[0]
		object["color"] = sub[1]
		object["shade"] = shade[2]
	elif type == 17:
		pass
	elif type == 18:
		pass
	elif type == 19:
		pass
	elif type == 20:
		pass
	elif type == 21:
		pass
	elif type == 22:
		object["type"] = "computer select"
		sub = unpack("> ii 16x", values[8])
		object["screen"] = sub[0]
		object["line"] = sub[1]
	elif type == 23:
		pass

	return object
