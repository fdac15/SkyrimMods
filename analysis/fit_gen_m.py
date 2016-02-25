#Added - none

#list of remaining tags - 
tags = ["Chargen","Companion Friendly","Companions","Compilation","For female characters","For male characters","Gameplay Effects/Changes","Official","Performance Optimization","Poses","Related to horses","Related to MLP","Related to Movies/TV/Other Games","Related to vampires","Replacer","Solstheim","Cheating","Fair and balanced","Unbalanced","BAB Bodybase","Bodyslide Preset","EC/HGEC Bodybase","Robert Female Bodybase","Robert Male Bodybase","TFF/UFF Bodybase","Animation - Modified","Animation - New","Audio - Music","Audio - Sound FX","Audio - Voices","Birthsigns","Body models","Classes component","Environment - Other","Environment - Sky","Environment - Water","Environment - Weather","Face models","Guilds / Factions","Hair","Leveled Lists","Lighting","New Lands","New models","New textures","Quests","Races - Modified","Races - New","Scripted Events","Video","Anime","Humor, Joke or Just for Fun","Lore-Friendly","Not Lore-Friendly","Not Safe For Work","Nudity","Saved games","Sexy/Skimpy","Translation","Unrealistic","Czech","English","French","German","Italian","Japanese","Other languages","Polish","Russian","Spanish","Armor - Shields","Books","Clothing","Clothing - Female","Clothing - Male","Creatures","Creatures - Rideable","Items - Apparatus","Items - Clutter","Items - Furniture","Items - Ingredients","Items - Leveled","Locations - Buildings","Locations - Caverns","Locations - Dungeons","Locations - Player-Owned","Locations - World Map","Magic - Enchantments","Magic - Potions","Magic - Spells","NPC Trainers","NPC Vendors","NPCs","Plants / Foliage","Weapons","Bloodmoon","Tribunal","Modder's Resource","Non-Playable Resource","Tutorials for Modders","Tutorials for Players","User Interface","Utilities for Modders","Utilities for Players","none"]


import csv
import numpy as np
import json

# open the file in universal line ending mode 
with open('morrowind.csv', 'rU') as infile:
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
outhead = 'Mod,Udl,time,Pop1,Pop10,Chargen,CompanionFriendly,Companions,Compilation,Forfemalecharacters,Formalecharacters,GameplayEffectsChanges,Official,PerformanceOptimization,Poses,Relatedtohorses,RelatedtoMLP,RelatedtoMoviesTVOtherGames,Relatedtovampires,Replacer,Solstheim,Cheating,Fairandbalanced,Unbalanced,BABBodybase,BodyslidePreset,ECHGECBodybase,RobertFemaleBodybase,RobertMaleBodybase,TFFUFFBodybase,Animation_Modified,Animation_New,Audio_Music,Audio_SoundFX,Audio_Voices,Birthsigns,Bodymodels,Classescomponent,Environment_Other,Environment_Sky,Environment_Water,Environment_Weather,Facemodels,GuildsFactions,Hair,LeveledLists,Lighting,NewLands,Newmodels,Newtextures,Quests,Races_Modified,Races_New,ScriptedEvents,Video,Anime,HumorJokeorJustforFun,Lore_Friendly,NotLore_Friendly,NotSafeForWork,Nudity,Savedgames,SexySkimpy,Translation,Unrealistic,Czech,English,French,German,Italian,Japanese,Otherlanguages,Polish,Russian,Spanish,Armor_Shields,Books,Clothing,Clothing_Female,Clothing_Male,Creatures,Creatures_Rideable,Items_Apparatus,Items_Clutter,Items_Furniture,Items_Ingredients,Items_Leveled,Locations_Buildings,Locations_Caverns,Locations_Dungeons,Locations_Player_Owned,Locations_WorldMap,Magic_Enchantments,Magic_Potions,Magic_Spells,NPCTrainers,NPCVendors,NPCs,PlantsFoliage,Weapons,Bloodmoon,Tribunal,ModdersResource,Non_PlayableResource,TutorialsforModders,TutorialsforPlayers,UserInterface,UtilitiesforModders,UtilitiesforPlayers,none\n'
outl = ''



with open("../morrowind_data/Morrowind_taglist.json","r") as f:
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

with open('fit_data_m.csv','w') as f:
    f.write(outf)