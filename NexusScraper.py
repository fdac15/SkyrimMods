import time, json, requests, os
from bs4 import BeautifulSoup

#define a timer which will be used to 
#regulate the speed at which pages will be
#retrieved

#pages retrieved/sec = (1/self.mtime)
class StopWatch:
    def __init__(self, time):
        self.mtime = time
    def start(self):
        ctime = time.time()+self.mtime
        while(ctime > time.time()):
            pass
        
#container class for information on mod
class ModBlock:
    def __init__(self,html=None):
        if html != None:
            try:
                self.from_html(html)
            except AttributeError:
                raise AttributeError
    def print_mod(self):
        print('{0}: {1}'.format('url', self.url))
        print('{0}: {1}'.format('likes', self.likes))
        print('{0}: {1}'.format('downloads', self.downloads))
        print('{0}: {1}'.format('name', self.name))
        print('{0}: {1}'.format('description', self.des))
        print('{0}: {1}'.format('created', self.created))
        print('{0}: {1}'.format('updated', self.update))
        print('{0}: {1}'.format('created by', self.creator))
    #should be an entry from get_nexus_mods
    def from_html(self, html):
        self.url = html.find('a', class_='image bubble-open pb-hover pb-left pb-ajax pb-forceclose', href=True)['href']
        self.likes = html.find('span', class_='likes').text
        self.downloads = html.find('span', class_='downloads').text
        self.name= html.find('a', class_='title')['title']
        self.des= html.find('div', class_=None).text
        self.created = html.find('div', class_='category-file-hover-released').text
        self.update = html.find('div', class_='category-file-hover-updated').text
        self.creator = html.find('a', class_='user').text
    #len(mlist) = 8
    def from_list(self, mlist):
        self.url = mlist[0]
        self.likes = mlist[1]
        self.downloads = mlist[2]
        self.name = mlist[3]
        self.des = mlist[4]
        self.created = mlist[5]
        self.update = mlist[6]
        self.creator = mlist[7]
    def get_id(self):
        id = [s for s in self.url.split('/') if s.isdigit()]
        return id[0]
    def to_list(self):
        data = [str(self.url), str(self.likes), str(self.downloads), str(self.name), '\''+str(self.des)+'\'', str(self.created), str(self.update), str(self.creator)]
        return data

#gets a list of the nexus mods at url
def get_nexus_mods(url):
    page = requests.get(url)
    
    if page.status_code != 200:
        print('bad error code')
        return None
    
    soup = BeautifulSoup(page.text, 'html5lib')

    blockList = soup.find('ul', class_="block-list")
    popboxes = blockList.find_all('li', class_='popbox')
    
    return popboxes

#returns a list of modblocks from pages start to end (inclusive)
#grabs pages at a rate of rr/sec
#both start and end should be a positive integer, start < end
#verbose decides whether to print status or not
#site is the name of the site you wish to gather from. multi-word names should be pushed
#together. ex) 'worldoftanks'
def get_nexus_mods_from_pages(start = 1, end = 1, rr = 1, site='skyrim',verbose=False):
    timer = StopWatch(rr)
    mods = []
    for i in range(start, end+1):
        if verbose:
            print('\rgetting page {0}/{1}'.format(i,end), end=' ')

        timer.start()
        url = 'http://www.nexusmods.com/'+site+'/mods/searchresults/?src_order=3&src_sort=0&src_view=1&src_tab=1&src_language=0&page='+str(i)+'&pUp=1'
        
        modList = get_nexus_mods(url)
        if modList == None:
            print('no mods on page {0}\nare you sure you\'re in range?'.format(url))
        for e in modList:
            try:
                mod = ModBlock(e)
            except AttributeError:
                continue
            mods.append(ModBlock(e))
    if verbose:
        print('\ndone')
    return mods

#mlist is a list of ModBlocks.
#This function writes mlist to a text file
def modblock_to_json(mlist=[], name = 'mods.json', mode='w'):
    jall = {}
    for mod in mlist:
        jall.update({mod.get_id(): mod.to_list()})
        
    data = {}
    if mode == 'a':
        if os.path.isfile(name):
            data = json_to_modblock(name)
            for mod in data:
                jall.update({mod.get_id(): mod.to_list()})
        
    with open(name, mode) as outfile:
        json.dump(jall, outfile)

#returns a list of modblocks generated from name
def json_to_modblock(name='mods.json'):
    with open(name, 'r') as infile:
        jall = json.loads(infile.read())
    
    jmods = []
    for mod in jall.values():
        modblock = ModBlock()
        modblock.from_list(mod)
        jmods.append(modblock)
    return jmods
#returns the page views of mod
def get_page_views(mod):
    try:
        page = requests.get(mod.url)
    except:
        return ''
    
    soup = BeautifulSoup(page.text, 'html5lib')
    return soup.find('p', class_='file-total-views').find('strong').text

def pageviews_to_json(mods, name='skyrim_pageviews.json', start=0, end=1, rr=0.1):
    timer = StopWatch(rr)
    pageviews = {}
    for i in range(start, end):
        timer.start()
        pageviews.update({mods[i].get_id(): get_page_views(mods[i])})
    with open(name, 'w') as outfile:
        json.dump(pageviews,outfile)
        
def get_page_views_range(mods,start=0, end=1, rr=0.1):
    timer = StopWatch(rr)
    pageviews = []
    for i in range(start,end):
        timer.start()
        pageviews.append(get_page_views(mods[i]))
        
    return pageviews