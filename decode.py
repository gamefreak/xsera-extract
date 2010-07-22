def bitfield(field, table):
	dict = {"hex": field}
	for i in range(0,31):
		if table[i] != "":
			if field & 0x1 << i:
				dict[table[i]] = True
			else:
				dict[table[i]] = False
	return dict

def fixed(value):
	return value/256.0
