#! /usr/bin/python

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

print "ret =",
format.object(obac.parse(file,1))
