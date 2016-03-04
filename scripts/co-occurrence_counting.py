import json, csv, sys
from collections import Counter
from math import sqrt

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

#get the total tags used
tag_total = sum([tag_count for tag_count in tag_counter.values()])

#next three blocks write a csv file for each cooccurence

header = ['Tag_Tuple', 'Tag1_Count','Tag2_Count','Co-Occurency_Count', 'P1',
	  'P2', 'P12', 'P1*P2-P12', '|d|/std1','|d|/std2', '|d|/std1+std2']
writer = csv.DictWriter(f=open(csv_file,'w'), fieldnames=header)

#write the csv file
writer.writeheader()
for tag in cooccurence_counter.keys():
    P1 = round(tag_counter[tag[0]]/tag_total, 6)
    P2 = round(tag_counter[tag[1]]/tag_total, 6)
    P12= round(cooccurence_counter[tag]/tag_total, 6)

    writer.writerow(
                 {header[0]: tag,
                  header[1]: tag_counter[tag[0]],
                  header[2]: tag_counter[tag[1]],
                  header[3]: cooccurence_counter[tag],
                  header[4]: P1,
		  header[5]: P2,
		  header[6]: P12,
		  header[7]: P1*P2-P12,
		  header[8]: (abs(P1*P2-P12)/sqrt((P1*(1-P1))/tag_total)),
		  header[9]: (abs(P1*P2-P12)/sqrt((P2*(1-P2))/tag_total)),
		  header[10]:(abs(P1*P2-P12)/sqrt(((P2*(1-P2))+(P1*(1-P1)))/tag_total))
		}
    )
