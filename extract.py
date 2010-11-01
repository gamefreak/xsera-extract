#! /usr/bin/python -B

from sys import	argv

import bsob
import obac
import race
import snbf
import sncd
import snro
import snit
import sprite

import format

types = [
		("bsob", bsob, "objects"),
		("obac", obac, "actions"),
		("sncd", sncd, "conditions"),
		("snro", snro, "scenarios"),
		("snbf", snbf, "briefings"),
		("snit", snit, "initials"),
		("race", race, "race"),
		]

data = {}

for ext, func, name in types:
	file = open("./data/500." + ext, "rb")
	data[name] = {}
	obj = func.parse(file,0)
	ctr = 0
	while obj != None:
		data[name][ctr] = obj
		ctr = ctr + 1
		obj = func.parse(file, ctr)
	file.close()
data["sprites"] = dict(sprite.generateList())
print "data =",
format.object(data)
