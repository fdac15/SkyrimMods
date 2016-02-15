import json, requests, os, locale
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from time import sleep

#set the locale to US
locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )
        
#container class for information on mod
class ModBlock:
    def __init__(self,html=None):
        self.views = 'None'
        self.udownloads = 'None'
        if html != None:
            try:
                self.from_html(html)
            except AttributeError:
                raise AttributeError
    def print_mod(self):
        print('{0}: {1}'.format('url', self.url))
        print('{0}: {1}'.format('likes', self.likes))
        print('{0}: {1}'.format('downloads', self.downloads))
        print('{0}: {1}'.format('unique dls', self.udownloads))
        print('{0}: {1}'.format('page views', self.views))
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
    #len(mlist) = 10
    def from_list(self, mlist):
        self.url = mlist[0]
        self.likes = mlist[1]
        self.downloads = mlist[2]
        self.name = mlist[3]
        self.des = mlist[4]
        self.created = mlist[5]
        self.update = mlist[6]
        self.creator = mlist[7]
        self.udownloads = mlist[8]
        self.views = mlist[9]
    def get_id(self):
        id = [s for s in self.url.split('/') if s.isdigit()]
        return id[0]
    def to_list(self):
        data = [str(self.url), str(self.likes), str(self.downloads), str(self.name), '\''+str(self.des)+'\'', str(self.created), str(self.update), str(self.creator), str(self.udownloads), str(self.views)]
        return data
    def get_pv_ud(self):
        try:
            page = requests.get(self.url)
        except:
            return
        soup = BeautifulSoup(page.text, 'html5lib')
        try:
            self.views = soup.find('p', class_='file-total-views').find('strong').text
            self.udownloads = soup.find('p', class_='file-unique-dls').find('strong').text
        except:
            return
        
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
    mods = []
    for i in range(start, end+1):
        if verbose:
            print('\rgetting page {0}/{1}'.format(i,end), end=' ')

        sleep(rr)
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
        
    if mode == 'l':
        return jall
    if mode == 'w':
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

#modes are " 'des', 'name', 'creator' "
#returns a list of two-tuple entries defined by a word-count pair.
#this list is of the most used words. by passing mode='creator'
#you can see how many mods a particular user has created
#if write=True, a json file is written as name
def most_used(mods=[],mode='des', write=False, name='most_used.json'):
    wordCount = {}
    tokens = []
    
    stopwords = ["'","''",'"','the','and',',','.','to','a','for','of','in','is','you','with','This','!','?','that','A','(',')',
              'from','it','I',"'s",'by','you','your',"you're",':','on','as','The','can','-','this','be','are','or',
              'will','have',"``",'an','my','at','so','not','but','into','some','...','just','It','--','them','also',
              'has',"n't",'which','Which','do','de','only','i','who','what','when','where','why',
              'if','was','&','You',']','[','their','they','http','/','\\',';','@','#','$','%','^','*','~','{','}','|',
              '+','=','<','>','he','she','his','her','hers','to','too','him',"'v","'re","'d"]
    for mod in mods:
        if mode == 'creator':
            tokens = word_tokenize(mod.creator.lower())
        elif mode == 'name':
            tokens = word_tokenize(mod.name.lower())
        else:
            tokens = word_tokenize(mod.des.lower())

        for token in tokens:
            if token in stopwords:
                continue
            if token in wordCount:
                wordCount[token]+=1
            else:
                wordCount.update({token:1})
                
    stuff = list(wordCount.items())
    sortedWordCount = sorted(stuff, key=lambda e: e[1])
    sortedWordCount.reverse()
    
    if write:
        with open(name,'w') as file:
            json.dump(sortedWordCount,file)
    
    return sortedWordCount

#returns a dictionary keyed in on creator names. values are the id's of the mods they created
def sort_by_creator(mods=[], write=False,name='sort_by_creator.json'):
    creators = {}
    for mod in mods:
        if mod.creator in creators:
            creators[mod.creator].append(mod.get_id())
        else:
            creators.update({mod.creator: [mod.get_id()]})
            
    if write:
        with open(name,'w') as file:
            json.dump(creators,file)
            
    return creators

#modes are udl, dl, pv, likes, name
def sort_by(mods=[], mode='udl'):
    for mod in mods:
        #these buggers are caused by nexus,
        #so I am explicitly handling them as needed
        if mod.udownloads == '':
             mod.udownloads = mod.downloads
        if mod.views == '':
             mod.views = '-1'
    #setup the key for sorting
    if mode == 'udl':
        key = lambda mod: locale.atoi(mod.udownloads)
    elif mode == 'dl':
        key = lambda mod: locale.atoi(mod.downloads)
    elif mode == 'pv':
        key = lambda mod: locale.atoi(mod.views)
    elif mode == 'name':
        key = lambda mod: mod.name
    else:
        key = lambda mod: locale.atoi(mod.likes)
    sorted_mods = sorted(mods, key=key)
    sorted_mods.reverse()
    return sorted_mods