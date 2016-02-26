"""
This script must have 2 command line arguments. 1 must be the taglist file,
2 must be the name of an ouput .csv file.

This script generates a table of boolean values based on whether a tag appears in a mod or not, and writes that information to a .csv file
"""

import json, numpy, sys, csv

if(len(sys.argv) < 3):
    print("not enough arguments given")
    print("usage: python Mod_Has_Tag.py taglist.json output.csv")
    exit()

#get tags and mods
tag_set = {}
mods = ()
data = {}

with open(sys.argv[1]) as file:
    data = json.load(file)

mods = tuple(data.keys())
tag_set = set({e for taglist in data.values() for e in taglist})

#generate table
bools = []
for mod in mods:
    temp = []
    for tag in tag_set:
        temp.append(1) if tag in data[mod] else temp.append(0)

    bools.append(temp)

#write table to file
writer = csv.DictWriter(open(sys.argv[2],'w'), fieldnames=list(tag_set))
writer.writeheader()
for row in bools:
    writer.writerow({list(tag_set)[i]: row[i] for i in range(len(row))})
