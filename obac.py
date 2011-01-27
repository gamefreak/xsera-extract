#! /usr/bin/python

from struct import unpack
import decode

size = 48
format = ">b ? IIhihh 4x 24s"

def parse(file, id = None):
	data = file.read(size)
	try:
		values = unpack(format, data)
	except:
		return None
	
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
	elif type == 1 or type == 17:
		if type == 17:
			object["type"] = "create object set destination"
		else:
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
		sub = unpack(">B x i? x iiii", values[8])
		object["priority"] = sub[0]
		object["persistence"] = sub[1]
		object["is absolute"] = sub[2]
		object["volume"] = sub[3]
		object["volume range"] = sub[4]
		object["sound id"] = sub[5]
		object["sound range"] = sub[6]
	elif type == 3:
		object["type"] = "alter"
		stype, relative, min, range = unpack("> B?ii 14x", values[8])
		if stype == 0:
			object["alter type"] = "health"
			object["value"] = min
		elif stype == 1:
			object["alter type"] = "velocity"
			object["relative"] = relative
			object["minimum"] = min
			object["range"] = range
		elif stype == 2:
			object["alter type"] = "thrust"
			object["relative"] = relative
			object["minimum"] = min
			object["range"] = range
		elif stype == 3:
			object["alter type"] = "max thrust"
			object["value"] = min
		elif stype == 4:
			object["alter type"] = "max velocity"
			object["value"] = min
		elif stype == 5:
			object["alter type"] = "max turn rate"
			object["value"] = min
		elif stype == 6:
			object["alter type"] = "location"
			object["relative"] = relative
			object["minimum"] = min
			object["range"] = range
		elif stype == 7:
#I don't think this is used in the scenario so I can't really test it
			object["alter type"] = "scale"
			object["value"] = min
		elif stype == 8:
			object["alter type"] = "pulse weapon"
			object["id"] = min
		elif stype == 9:
			object["alter type"] = "beam weapon"
			object["id"] = min
		elif stype == 10:
			object["alter type"] = "special weapon"
			object["id"] = min
		elif stype == 11:
			object["alter type"] = "energy"
			object["value"] = min
		elif stype == 12:
			object["alter type"] = "owner"
			object["use objects owner"] = relative
			object["value"] = min
		elif stype == 13:
			object["alter type"] = "hidden"
			object["minimum"] = min
			object["range"] = range
		elif stype == 14:
			object["alter type"] = "cloak"
		elif stype == 15:
			object["alter type"] = "offline"
			object["minimum"] = min
			object["range"] = range
		elif stype == 16:
			object["alter type"] = "current turn rate"
			object["minimum"] = min
			object["range"] = range
		elif stype == 17:
			object["alter type"] = "base type"
			object["retain ammmo count"] = relative
			object["id"] = min
		elif stype == 18:
			object["alter type"] = "active condition"
			object["condition true"] = relative #find better name
			object["minimum"] = min
			object["range"] = range
		elif stype == 19:
			object["alter type"] = "occupation"
			object["value"] = min
		elif stype == 20:
			object["alter type"] = "absolute cash"
			object["use objects owner"] = relative
			object["value"] = min
			object["player"] = range
		elif stype == 21:
			object["alter type"] = "age"
			object["relative"] = relative
			object["minimum"] = min
			object["range"] = range
		elif stype == 22:
			object["alter type"] = "absolute location"
			object["relative"] = relative
			object["x"] = min
			object["y"] = range
	elif type == 4:
		object["type"] = "make sparks"
		sub = unpack(">ii i B 11x", values[8])
		object["count"] = sub[0]
		object["velocity"] = sub[1]
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
		object["player"] = sub[0]
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
		object["type"] = "set destination"
	elif type == 13:
		object["type"] = "activate special"
	elif type == 14:
		object["type"] = "activate pulse"
	elif type == 15:
		object["type"] = "activate beam"
	elif type == 16:
		object["type"] = "color flash"
		sub = unpack("> i BB 18x", values[8])
		object["duration"] = sub[0]
		object["color"] = sub[1]
		object["shade"] = sub[2]
	elif type == 17:
		#see action #1 (create object action)
		pass
	elif type == 18:
		object["type"] = "nil target"
	elif type == 19:
		object["type"] = "disable keys"
		sub = unpack("> I 20x", values[8])
		object["key mask"] = sub[0]
	elif type == 20:
		object["type"] = "enable keys"
		sub = unpack("> I 20x", values[8])
		object["key mask"] = sub[0]
	elif type == 21:
		object["type"] = "set zoom level"
		sub = unpack("> i 20x", values[8])
		object["value"] = sub[0]
	elif type == 22:
		object["type"] = "computer select"
		sub = unpack("> ii 16x", values[8])
		object["screen"] = sub[0]
		object["line"] = sub[1]
	elif type == 23:
		object["type"] = "assume initial object"
		sub = unpack("> i 20x", values[8])
		object["id"] = sub[0]
	return object
