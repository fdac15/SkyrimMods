import json, csv, sys
from collections import Counter

try:
    json_file = str(sys.argv[1])
    csv_file = str(sys.argv[2]) 
except:
    print("not enough arguments given")
    print("python co-occurence_counting.py json_file_name csv_file_name")
    exit()

tags = json.load(open(json_file))

cooccurence_counter = Counter()
tag_counter = Counter()

#get a count of all tags and their cooccurences
for v in tags.values():
    tag_counter.update(v)
    for i in range(len(v)):
        for j in range(i+1, len(v)):
            cooccurence_counter.update(((v[i],v[j]),))

#get the ratio of tags for their cooccurences

ratio_counter = {}
for tag in cooccurence_counter.keys():
    ratio_counter[tag] = (tag_counter[tag[0]]/tag_counter[tag[1]])

#next three blocks write a csv file for each cooccurence

header = ['tag_tuple', 'tag1_count','tag2_count', 'ratio']
writer = csv.DictWriter(f=open(csv_file,'w'), fieldnames=header)

#write the csv file
writer.writeheader()
for tag in cooccurence_counter.keys():
    writer.writerow(
                 {header[0]: tag,
                 header[1]: tag_counter[tag[0]],
                 header[2]: tag_counter[tag[1]],
                 header[3]: ratio_counter[tag]}
    )

