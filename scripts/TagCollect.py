### The code is not running from Ipython Notebook, so writing standalone script###

#define a timer which will be used to 
#regulate the speed at which pages will be
#retrieved

#pages retrieved/sec = (1/self.mtime)

import time
import sys
import os
import json
import requests
from bs4 import BeautifulSoup 


class StopWatch:
    def __init__(self, time):
        self.mtime = time
    def start(self):
        ctime = time.time()+self.mtime
        while(ctime > time.time()):
            pass
with open('../dragon_age_data/dai/dragon_age_inquisition_mods_all.json','r') as jfile:
    mod_json = json.loads(jfile.read())
    


timer = StopWatch(0.2)
timer2 = StopWatch(10)

if os.path.isfile('checked_dai.txt'):
    with open('checked_dai.txt','r') as f:
        checked = f.read().split(',')
else:
    checked = []
print (len(checked), 'files already done')
    
fstr = '{'
l = len(mod_json.keys())
print (l)
k = 1
try:
    for key in mod_json:
        
        if str(key) not in checked:
            mod_tag = {}
            url = 'http://www.nexusmods.com/dragonageinquisition/ajax/modtags/?id='+str(key)
            timer.start()
            
            if (k%500) == 0:
                    timer2.start()

            page = requests.get(url)

            if page.status_code != 200:
                print ('ERROR!!!')
                sys.exit()

            soup = BeautifulSoup(page.text, 'html5lib')

            worklist = soup.findAll("span", class_="green")

            i = 0
            taglist = []
            for ele in worklist:
                s = BeautifulSoup(str(ele), 'html5lib')

                if i == 0: pass
                elif (i%2) == 0:
                    taglist.append(s.text)

                

                i += 1

            mod_tag [key] = taglist
            
            checked.append(str(key))

            print ('Completed making Tag List for ',key)
            per = (k/l)*100
            print ( '%.2f  completed' % k)
            k += 1
            fstr += '"'+str(key) + '":' + (str(taglist).replace('\'','"')).replace('"s', "'s")+','

    fstr = fstr[:-1]+'}'
    
    checked = list(set(checked))
    
    checked_str = ','.join(str (k) for k in checked)
    with open ('taglist_dai.json','a') as tagfile:
        tagfile.write(fstr)
    with open('checked_dai.txt','w') as f:
            f.write(checked_str)
        
except:
    fstr = fstr[:-1]
    checked_str = ','.join(str (k) for k in checked)
    with open ('taglist_dai.json','a') as tagfile:
        tagfile.write(fstr)
    with open('checked_dai.txt','w') as f:
        f.write(checked_str)
       
    print ('Connection Error !!!!!!!')
    print (len(checked), 'mods are listed')
        