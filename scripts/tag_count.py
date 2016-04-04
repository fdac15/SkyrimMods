'''takes two  command line arguments, the .json filename of a taglist_by_mod file and an output file.
   counts the number of mods each tag has, and outputs results to a json file
'''

import json, sys

if len(sys.argv) < 3:
  print('not enough arguments')

with open(sys.argv[1]) as file:
  data = json.load(file)

count = {item[0]: len(item[1]) for item in data.items()}

with open(sys.argv[2], 'w') as file:
  json.dump(count, file)
