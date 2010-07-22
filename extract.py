#! /usr/bin/python

import bsob
import format

file = open("./data/500.bsob", "rb")

print "ret =",
format.object(bsob.parse(file,0))
format.object(bsob.parse(file,1))
