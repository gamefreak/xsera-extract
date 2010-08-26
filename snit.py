from struct import unpack
import strings
import decode

attributes = [
		"", "", "", "",
		"fixed race", "initially hidden", "", "",
		"", "is player ship", "", "",#????
		"", "", "", "",
		"", "", "", "",
		"", "", "", "",
		"", "static destination", "", "",
		"", "", "", "",
]


size = 108
format = "> iiii 2i i 4i 12i 3i I"

def parse(file, id):
	data = file.read(size)
	values = unpack(format, data)
	
	object = {}
	object["type"] = values[0]
	object["owner"] = values[1]
	#These do not seem to seem to be used in the scenario
	#so I have disabled them.
	#object["real object number"] = values[2]
	#object["real object id"] = values[3]
	object["position"] = {
			"x": values[4],
			"y": values[5],
			}
	object["earning"] = decode.fixed(values[6])
	object["distance range"] = values[7]
	object["rotation"] = {
			"minumum": values[8],
			"range": values[9],
			}
	object["sprite id override"] = values[10]
	object["builds"] = {}
	for i in range(11,22):
		if values[i] >= 1:
			object["builds"][i-11] = values[i]
	object["initial destination"] = values[23]
	if values[24] >= 1: #and values[24] != 4400: #stupid
		try:
			object["foo"] = strings.db[str(values[24])][values[25]]
		except:
			pass #I will deal with this later, only if it causes problems
	object["attributes"] = decode.bitfield(values[26], attributes)
	return object
