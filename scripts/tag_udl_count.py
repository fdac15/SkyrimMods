'''generates a two column table describing the total unique downloads for each tag category.
'''

import json, sys, locale

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def tag_udl_count(f1, f2, p=False,f3=''):
  mods = json.load(open(f1))
  tags = json.load(open(f2))
  
  udl = {}
  try:
    for tag in tags.keys():
      sum = 0
      for mod in tags[tag]:
        if mods[mod][8] == '' or mods[mod][8] == 'None':
          continue
        sum += locale.atoi(mods[mod][8])
      udl[tag] = sum
  except ValueError as e:
   print(e)

  if p:
    with open(f3,'w') as f:
      for i in udl.items():
        f.write('{0[0]}:{0[1]}\n'.format(i))
  return udl

