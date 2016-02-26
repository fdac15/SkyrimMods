"""
This script must have 3 command line arguments. 1 must be the taglist file,
2 the taglist_by_mod file, 3 must be the name of an ouput .csv file.

This script generates a table of boolean values based on whether a tag appears in a mod or not, and writes that information to a .csv file
"""

import json, numpy, sys, csv

if(len(sys.argv) < 4):
    print("not enough arguments given")
    print("usage: python Mod_Has_Tag.py taglist.json taglist_by_mod.json output.csv")
    exit()

#get tags and mods

tags = ()
with open(sys.argv[2]) as file:
    data = json.load(file)
    tags = tuple(data.keys())
    
mods = ()
with open(sys.argv[1]) as file:
    data = json.load(file)
    mods = tuple(data.keys())


data = {}
with open(sys.argv[1]) as file:
    data = json.load(file)

#generate table
bools = []
for mod in mods:
    temp = []
    for tag in tags:
        if tag in data[mod]:
            temp.append(1)
        else:
            temp.append(0)
    bools.append(temp)

#write table to file
writer = csv.DictWriter(open(sys.argv[3],'w'), fieldnames=tags)

writer.writeheader()
for row in bools:
    writer.writerow({tags[i]: row[i] for i in range(len(row))})
