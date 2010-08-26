#! /usr/bin/python

from sys import	argv

import bsob
import obac
import race
import snbf
import snro
import snit

import format

types = {
		"bsob": bsob,
		"obac": obac,
		"snro": snro,
		"snbf": snbf,
		"snit": snit,
		"race": race,
		}

data = {}

for ext, func in types.items():
	file = open("./data/500." + ext, "rb")
	data[ext] = {}
	obj = func.parse(file,0)
	ctr = 0
	while obj != None:
		data[ext][ctr] = obj
		ctr = ctr + 1
		obj = func.parse(file, ctr)
	file.close()
format.object(data)
