#! /usr/bin/python

from sys import	argv

import bsob
import obac
import race
import snbf
import snro

import format

#file = open("./data/500.bsob", "rb")
#file = open("./data/500.race", "rb")
#file = open("./data/500.snbf", "rb")
#file = open("./data/500.snro", "rb")
file = open("./data/500.obac", "rb")
if len(argv) > 1:
	count = int(argv[1])
else:
	count = 1
for id in range(0, count):
	format.object(obac.parse(file,1))
