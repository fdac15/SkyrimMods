import sys, json

try:
    with open(sys.argv[1], 'r') as file:
        tags = json.load(file)
except:
    print('could not open file {0}'.format(sys.argv[1]))
    exit()
    
for key in tags.keys():
    if len(tags[key]) == 0:
        tags[key].append('none')

with open(sys.argv[1], 'w') as file:
    json.dump(tags, file)