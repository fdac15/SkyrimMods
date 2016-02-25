#list of remaining tags - 
tags = ["Compilation","Gameplay Effects/Changes","Official","Performance Optimization","Related to MLP","Audio - Music","Audio - Sound FX","Audio - Voices","Body models","Environment - Other","Environment - Sky","Environment - Water","Environment - Weather","Face models","New models","New textures","Quests","Scripted Events","Skills","Anime","Humor, Joke or Just for Fun","Not Safe For Work","Nudity","Saved games","Sexy/Skimpy","Translation","Unrealistic","Czech","English","French","German","Italian","Japanese","Other languages","Polish","Russian","Spanish","Modder's Resource","Non-Playable Resource","Tutorials for Modders","Tutorials for Players","User Interface","Utilities for Modders","Utilities for Players","none"]

import csv
import numpy as np
import json

# open the file in universal line ending mode 
with open('dai.csv', 'rU') as infile:
# read the file as a dictionary for each row ({header : value})
  reader = csv.DictReader(infile)
  data = {}
  for row in reader:
    for header, value in row.items():
      try:
        data[header].append(value)
      except KeyError:
        data[header] = [value]
        
mods = data['Mod']
time = data['time']
udl = list(map(int, data['unique_dl']))

#Two popularity outputs, top 10% and top 1%

ua = np.array(udl)
p1 = int(np.percentile(ua, 99))
p10 = int(np.percentile(ua, 90)) 


#Header of the output csv
outhead = 'Mod,Udl,time,Pop1,Pop10,Compilation,GameplayEffectsChanges,Official,PerformanceOptimization,RelatedtoMLP,Audio_Music,Audio_SoundFX,Audio_Voices,Bodymodels,Environment_Other,Environment_Sky,Environment_Water,Environment_Weather,Facemodels,Newmodels,Newtextures,Quests,ScriptedEvents,Skills,Anime,HumorJokeorJustforFun,NotSafeForWork,Nudity,Savedgames,SexySkimpy,Translation,Unrealistic,Czech,English,French,German,Italian,Japanese,Otherlanguages,Polish,Russian,Spanish,ModdersResource,Non_PlayableResource,TutorialsforModders,TutorialsforPlayers,UserInterface,UtilitiesforModders,UtilitiesforPlayers,none\n'
outl = ''

with open("../dragon_age_data/dai/taglist_dai.json","r") as f:
    tag_dict = json.load(f)
    
for i in range(len(mods)):
    mod = mods[i]
    dl = udl[i]
    tym = time[i]
    
    if (dl > p1): pop1 = '1'
    else: pop1 = '0'    

    if (dl > p10): pop10 = '1'
    else: pop10 = '0'  
        
    outl += mod+','+str(dl)+','+tym+','+pop1+','+pop10+','
    
    for ele in tags:
        if ele in tag_dict[mod]: outl += '1,'
        else: outl += '0,'
            
    outl = outl[:-1]+'\n'

outf = outhead+outl

with open('fit_data_dai.csv','w') as f:
    f.write(outf)