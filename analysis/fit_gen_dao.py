

#list of remaining tags - 
tags = ["Companion - Anders (DA2)","Companion - Aveline","Companion - Bethany","Companion - Carver","Companion - Fenris","Companion - Isabela","Companion - Merrill","Companion - Sebastian","Companion - Tallis","Companion - Varric","Chargen","Companion Friendly","Companions","Compilation","For DA2","For DAA","For DAO","For female characters","For male characters","Gameplay Effects/Changes","Official","Performance Optimization","Related to MLP","Related to Movies/TV/Other Games","Replacer","Cheating","Fair and balanced","Unbalanced","Companion - Anders","Companion - Justice","Companion - Mhairi","Companion - Nathaniel","Companion - Sigrun","Companion - Velanna","Companions - DA Origins","Companion - Alistair","Companion - Dog","Companion - Leliana","Companion - Loghain","Companion - Morrigan","Companion - New - Female","Companion - New - Male","Companion - Oghren","Companion - Shale","Companion - Sten","Companion - Wynne","Companion - Zevran","Animation - Modified","Animation - New","Audio - Music","Audio - Sound FX","Audio - Voices","Body models","Classes component","Environment - Other","Environment - Sky","Environment - Water","Environment - Weather","Face models","Hair","Lighting","New Lands","New models","New textures","Quests","Races - Modified","Races - New","Scripted Events","Singleplayer Campaign","Skills","Video","Anime","Humor"," Joke or Just for Fun","Lore-Friendly","Not Lore-Friendly","Not Safe For Work","Nudity","Saved games","Sexy/Skimpy","Translation","Unrealistic","Czech","English","French","German","Italian","Japanese","Other languages","Polish","Russian","Spanish","Armor - Shields","Books","Clothing","Clothing - Female","Clothing - Male","Creatures","Items - Apparatus","Items - Clutter","Items - Furniture","Items - Ingredients","Locations - Buildings","Locations - Caverns","Locations - Dungeons","Locations - Player-Owned","Locations - World Map","Magic - Enchantments","Magic - Potions","Magic - Spells","NPC Vendors","NPCs","Plants / Foliage","Weapons","Modder's Resource","Non-Playable Resource","Tutorials for Modders","Tutorials for Players","User Interface","Utilities for Modders","Utilities for Players","none"]

import csv
import numpy as np
import json

# open the file in universal line ending mode 
with open('dao.csv', 'rU') as infile:
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
outhead = 'Mod,Udl,time,Pop1,Pop10,Companion_Anders_DA2,Companion_Aveline,Companion_Bethany,Companion_Carver,Companion_Fenris,Companion_Isabela,Companion_Merrill,Companion_Sebastian,Companion_Tallis,Companion_Varric,Chargen,CompanionFriendly,Companions,Compilation,ForDA2,ForDAA,ForDAO,Forfemalecharacters,Formalecharacters,GameplayEffectsChanges,Official,PerformanceOptimization,RelatedtoMLP,RelatedtoMoviesTVOtherGames,Replacer,Cheating,Fairandbalanced,Unbalanced,Companion_Anders,Companion_Justice,Companion_Mhairi,Companion_Nathaniel,Companion_Sigrun,Companion_Velanna,Companions_DAOrigins,Companion_Alistair,Companion_Dog,Companion_Leliana,Companion_Loghain,Companion_Morrigan,Companion_New_Female,Companion_New_Male,Companion_Oghren,Companion_Shale,Companion_Sten,Companion_Wynne,Companion_Zevran,Animation_Modified,Animation_New,Audio_Music,Audio_SoundFX,Audio_Voices,Bodymodels,Classescomponent,Environment_Other,Environment_Sky,Environment_Water,Environment_Weather,Facemodels,Hair,Lighting,NewLands,Newmodels,Newtextures,Quests,Races_Modified,Races_New,ScriptedEvents,SingleplayerCampaign,Skills,Video,Anime,Humor,JokeorJustforFun,Lore_Friendly,NotLore_Friendly,NotSafeForWork,Nudity,Savedgames,SexySkimpy,Translation,Unrealistic,Czech,English,French,German,Italian,Japanese,Otherlanguages,Polish,Russian,Spanish,Armor_Shields,Books,Clothing,Clothing_Female,Clothing_Male,Creatures,Items_Apparatus,Items_Clutter,Items_Furniture,Items_Ingredients,Locations_Buildings,Locations_Caverns,Locations_Dungeons,Locations_Player_Owned,Locations_WorldMap,Magic_Enchantments,Magic_Potions,Magic_Spells,NPCVendors,NPCs,PlantsFoliage,Weapons,ModdersResource,Non_PlayableResource,TutorialsforModders,TutorialsforPlayers,UserInterface,UtilitiesforModders,UtilitiesforPlayers,none\n'
outl = ''

with open("../dragon_age_data/da/taglist_da.json","r") as f:
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

with open('fit_data_dao.csv','w') as f:
    f.write(outf)














