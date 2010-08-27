import os

def generateList():
	data = {}
	os.chdir("data/sprites")
	for item in os.listdir("."):
		if item != ".DS_Store":
			pair = item.split(" ",1)
			data[pair[0]] = pair[1]
	os.chdir("../..")
	return data
