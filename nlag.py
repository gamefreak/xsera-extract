from struct import unpack
import decode
import strings

flags = [
"is networkable", "custom objects", "custom races", "custom scenarios",
"is unoptimized", "", "", "",
"", "", "", "",
"", "", "", "",

"", "", "", "",
"", "", "", "",
"", "", "", "",
"", "", "", "",
		]

length = 1056
format = "> 4i B255s B255s B255s B255s 4I"

def parse(file, id=None):
	data = file.read(length)
	try:
		values = unpack(format, data)
	except:
		return -1
	
	object = {}
	object["in flare id"] = values[0]
	object["out flare id"] = values[1]
	object["player body id"] = values[2]
	object["energy blob id"] = values[3]
	object["download url"] = values[5][:values[4]]
	object["title"] = values[7][:values[6]]
	object["author name"] = values[9][:values[8]]
	object["author url"] = values[11][:values[10]]
	object["version"] = values[12]
	object["min version"] = values[13]
	object["flags"] = decode.bitfield(values[14], flags)
	#discard checksum
	return object
