'''takes two  command line arguments, the .json filename of a tagl_count file and an output file.
   creates a string with no. of occurrence as in the count
'''

import json, sys, re, math

if len(sys.argv) < 3:
  print('not enough arguments')

with open(sys.argv[1]) as file:
  data = json.load(file)

outstr = ''

for key in data.keys():
    key1 = re.sub(r'[ -/_]+','_',key)
    for i in range(int(math.log(data[key]))):
        outstr += key1 + ' '

with open(sys.argv[2], 'w') as file:
  file.write(outstr)