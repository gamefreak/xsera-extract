#! /usr/bin/python

import bsob
import race
import format

#file = open("./data/500.bsob", "rb")
file = open("./data/500.race", "rb")

print "ret =",
format.object(race.parse(file,0))
format.object(race.parse(file,1))
