from struct import unpack
import strings
import decode
import math

size = 38

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
				"x": base[1],
				"y": base[0]
				},
			"counter": {
				"player": base[0],
				"counter": base[1],
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
	return object
