#! /usr/bin/python

import bsob
import format

file = open("./data/500.bsob", "rb")

print "ret =",
format.object(bsob.parse(file))
format.object(bsob.parse(file))
