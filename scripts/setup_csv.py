import json
import datetime
with open('../skyrim_data/skyrim_mods_all.json') as f:
    j = json.load(f)

    
print ("Skyrim\n")
csv_str = 'Mod,likes,downloads,time,unique_dl,views,dl_dif\n'

for key in j.keys():
    rel_date = j[key][-5].split(' ')[1]
    date_part = rel_date.split('/')
    
    if (int(date_part[2]) < 2011):
        print (rel_date)
        continue
    
    rel_date = datetime.date(int(date_part[2]),int(date_part[1]),int(date_part[0]))

    today = datetime.date.today()
    date_diff = (today - rel_date).days
    
    if str(j[key][-1]) == '': continue
        
    if int(date_diff) < 90: continue
    
    if  (j[key][2] != '' and j[key][-2] != ''):
    
        dl_diff = int(j[key][2].replace(',','')) - int(j[key][-2].replace(',',''))
        
        if dl_diff <0 : continue
    
    
    temp = str(key)+','+str(j[key][1]).replace(',','')+','+str(j[key][2]).replace(',','')+','+str(date_diff)+','+str(j[key][-2]).replace(',','')+','+str(j[key][-1]).replace(',','')+','+str(dl_diff)+'\n'
    csv_str += temp

csv_str = csv_str[:-1]

with open('skyrim.csv','w') as f:
    f.write(csv_str)

    
print ('Oblivion\n')
with open('../oblivion_data/oblivion_mods_all.json') as f:
    j = json.load(f)
    
csv_str = 'Mod,likes,downloads,time,unique_dl,views,dl_dif\n'

for key in j.keys():
    rel_date = j[key][-5].split(' ')[1]
    date_part = rel_date.split('/')
    
    if (int(date_part[2]) < 2005):
        print (rel_date)
        continue
    
    rel_date = datetime.date(int(date_part[2]),int(date_part[1]),int(date_part[0]))

    today = datetime.date.today()
    date_diff = (today - rel_date).days
    
    if str(j[key][-1]) == '': continue
    if int(date_diff) < 90: continue
    
    if  (j[key][2] != '' and j[key][-2] != ''):
    
        dl_diff = int(j[key][2].replace(',','')) - int(j[key][-2].replace(',',''))
        
        if dl_diff <0 : continue
    

    temp = str(key)+','+str(j[key][1]).replace(',','')+','+str(j[key][2]).replace(',','')+','+str(date_diff)+','+str(j[key][-2]).replace(',','')+','+str(j[key][-1]).replace(',','')+','+str(dl_diff)+'\n'
    csv_str += temp

csv_str = csv_str[:-1]

with open('oblivion.csv','w') as f:
    f.write(csv_str)

    
print ('Morrowind\n')
with open('../morrowind_data/morrowind_mods_all.json') as f:
    j = json.load(f)
    
csv_str = 'Mod,likes,downloads,time,unique_dl,views,dl_dif\n'

for key in j.keys():
    rel_date = j[key][-5].split(' ')[1]
    date_part = rel_date.split('/')
    
    if (int(date_part[2]) < 2002):
        print (rel_date)
        continue
    
    rel_date = datetime.date(int(date_part[2]),int(date_part[1]),int(date_part[0]))

    today = datetime.date.today()
    date_diff = (today - rel_date).days

    if str(j[key][-1]) == '': continue
    
    if int(date_diff) < 90: continue
    
    if  (j[key][2] != '' and j[key][-2] != ''):
    
        dl_diff = int(j[key][2].replace(',','')) - int(j[key][-2].replace(',',''))
        
        if dl_diff <0 : continue
    
    temp = str(key)+','+str(j[key][1]).replace(',','')+','+str(j[key][2]).replace(',','')+','+str(date_diff)+','+str(j[key][-2]).replace(',','')+','+str(j[key][-1]).replace(',','')+','+str(dl_diff)+'\n'
    csv_str += temp

csv_str = csv_str[:-1]

with open('morrowind.csv','w') as f:
    f.write(csv_str)