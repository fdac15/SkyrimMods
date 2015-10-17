### The code is not running from Ipython Notebook, so writing standalone script###

#define a timer which will be used to 
#regulate the speed at which pages will be
#retrieved

#pages retrieved/sec = (1/self.mtime)

import time
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
with open('skyrim_mods_1.json','r') as jfile:
    mod_json = json.loads(jfile.read())
    


timer = StopWatch(0.1)

fstr = ''
l = len(mod_json.keys())
print (l)
k = 1
for key in mod_json:
    mod_tag = {}
    url = 'http://www.nexusmods.com/skyrim/ajax/modtags/?id='+str(key)+'&pUp=1&gid=110'
    timer.start()
    
    page = requests.get(url)
    
    if page.status_code != 200: print ('ERROR!!!')
    
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
    
    print ('Completed making Tag List for ',key)
    per = (k/l)*100
    print ( '%.2f percent completed' % per)
    k += 1
    fstr += '"'+str(key) + '":' + str(taglist).replace('\'','"') + ','

fstr = fstr[:-1]
with open ('taglist_1','w') as tagfile:
    tagfile.write(fstr)