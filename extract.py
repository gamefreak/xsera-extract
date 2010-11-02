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
data["sounds"] = {
	500: "ShotC",
	501: "ExplosionCombo",
	503: "explosn.02 short",
	510: "ZoomChange",
	511: "NaughtyBeep",
	512: "Lectro Zap Mixed",
	517: "WarpIn",
	518: "WarpOut",
	519: "SShot 1",
	520: "fighter launch",
	521: "Lectro Zap Mixed Low",
	522: "Stealth Off",
	523: "Stealth On",
	524: "Spark Thump",
	525: "Beep Buzzer copy.22",
	526: "thonk warp 1.1",
	527: "Thonk Warp 1.2",
	528: "Thonk Warp 1.3",
	529: "thonk warp 1.4",
	533: "RocketLaunchr",
	534: "Astrocrunch",
	537: "audemedon missile 2",
	538: "audem missile 1",
	539: "laser, elejeetian sound 2",
	541: "missile, elejeetian sound 1",
	542: "missile, elejeetian sound 3",
	543: "human laser 2",
	544: "human torpedo 1",
	545: "human laser 3",
	546: "human torpedo 2",
	547: "space blob sucks",
	549: "target drone laser",
	551: "target deactivate beep.snd",
	554: "heavy destroyer (cantharan).8",
	556: "saril destroyer",
	557: "human destroyer",
	558: "audemedon destroyer",
	559: "gaitori destroyer",
	560: "Stingy Whip Laser Misc",
	561: "22",
	563: "11.snd-1",
	564: "11.snd-2", #--[CHECK]
	565: "22.snd",
	566: "22.snd-1",
	567: "22.snd-2",
	568: "22.snd-3",
	569: "22.snd-4",
	570: "22.snd-5",
	9800: "jumpgate opens hifi copy",
	10312: "Let's Go",
	28853: "Beam Scan Modified",
	}
print "data =",
format.object(data)
