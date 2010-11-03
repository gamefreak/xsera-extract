from struct import unpack
import strings
import decode
import math

size = 38

flags = [
		"true only once", "initially true", "has been true", "",
		"", "", "", "",
		"", "", "", "",
		"", "", "", "",
		"", "", "", "",
		"", "", "", "",
		"", "", "", "",
		"", "", "", ""
		]

format = "> Bx 12s iiiiIi"

def parse(file, id = None):
	data = file.read(size)
	try:
		values = unpack(format, data)
	except:
		return None
	object = {}
	type = values[0]
	base = unpack(">3i", values[1])
	tags = {
			"point": {
				"x": base[0],
				"y": base[1]
				},
			"counter": {
				"player": base[0],
				"id": base[1],
				"amount": base[2],
				},
			"signed": base[0],
			"unsigned": unpack("> I 8x", values[1])[0],
			}
	if type == 0:
		object["type"] = "none"
	elif type == 1:
		object["type"]  = "location"
		object["location"] = tags["point"]
	elif type == 2:
		object["type"] = "counter"
		object["counter"] = tags["counter"]
	elif type == 3:
		object["type"] = "proximity"
		object["location"] = math.sqrt(tags["unsigned"])
	elif type == 4:
		object["type"] = "owner"
		object["value"] = tags["signed"]
	elif type == 5:
		object["type"] = "destruction"
		object["value"] = tags["signed"]
	elif type == 6:
		object["type"] = "age"
		object["value"] = tags["signed"]
	elif type == 7:
		object["type"] = "time"
		object["value"] = tags["signed"]
	elif type == 8:
		object["type"] = "random"
#		object["value"] = tags["signed"]
	elif type == 9:
		object["type"] = "half health"
#		object["value"] = tags["signed"]
	elif type == 10:
		object["type"] = "is auxiliary"
	elif type == 11:
		object["type"] = "is target"
	elif type == 12:
		object["type"] = "counter greater"
		object["counter"] = tags["counter"]
	elif type == 13:
		object["type"] = "counter not"
		object["counter"] = tags["counter"]
	elif type == 14:
		object["type"] = "distance greater"
		object["value"] = tags["unsigned"]
	elif type == 15:
		object["type"] = "velocity less than or equal"
		object["value"] = tags["signed"]
	elif type == 16:
		object["type"] = "no ships left"
		object["player"] = tags["signed"]
	elif type == 17:
		object["type"] = "current message"
		object["id"] = tags["point"]["x"]
		object["page"] = tags["point"]["y"]
	elif type == 18:
		object["type"] = "current computer selection"
		object["screen"] = tags["point"]["x"]
		object["line"] = tags["point"]["y"]
	elif type == 19:
		object["type"] = "zoom level"
		object["value"] = tags["signed"]
	elif type == 20:
		object["type"] = "autopilot"
	elif type == 21:
		object["type"] = "not autopilot"
	elif type == 22:
		object["type"] = "object being built"
	elif type == 23:
		object["type"] = "direct is subject target"
	elif type == 24:
		object["type"] = "subject is player"
	object["subject"] = values[2]
	object["direct"] = values[3]
	object["start"] = values[4]
	object["count"] = values[5]
	object["flags"] = decode.bitfield(values[6], flags)
#	object["direction"] = values[7] #UNUSED?
	return object
