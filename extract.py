#! /usr/bin/python

import bsob
import race
import snbf
import format

#file = open("./data/500.bsob", "rb")
#file = open("./data/500.race", "rb")
file = open("./data/500.snbf", "rb")

print "ret =",
format.object(snbf.parse(file,1))
format.object(snbf.parse(file,1))
format.object(snbf.parse(file,1))
format.object(snbf.parse(file,1))
