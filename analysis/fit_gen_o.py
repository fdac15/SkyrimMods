#Ignore Category: Language - coz too much in English, Requirements - coz doesn't describe any attributes of the mod, Balance - coz most are Fair and Balanced, Resources - coz relatively fewer in number   
#Other Ignore tags: Attributes - All faction tags, Related to MLP; Content and Realism - Saved Games, Translations; Components - Audio-Music, Races-New; Content and Realism - Humor,Jokes or Just for Fun
#Added - none

#list of remaining tags - 
tags = ["Anime",  "Lore-Friendly", "Not Lore-Friendly", "Not Safe For Work", "Nudity", "Sexy/Skimpy", "Unrealistic", "Armor - Shields", "Books", "Clothing", "Clothing - Female", "Clothing - Male", "Creatures", "Creatures - Rideable", "Items - Apparatus", "Items - Clutter", "Items - Furniture", "Items - Ingredients", "Items - Leveled", "Locations - Buildings", "Locations - Caverns", "Locations - Dungeons", "Locations - Player-Owned", "Locations - World Map", "Magic - Enchantments", "Magic - Potions", "Magic - Spells", "NPC Trainers", "NPC Vendors", "NPCs", "Plants / Foliage", "Weapons", "Animation - Modified", "Animation - New", "Audio - Sound FX", "Audio - Voices", "Birthsigns", "Body models", "Classes component", "Environment - Other", "Environment - Sky", "Environment - Water", "Environment - Weather", "Face models", "Guilds / Factions", "Hair", "Leveled Lists", "Lighting", "New Lands", "New models", "New textures", "Quests", "Races - Modified", "Scripted Events", "Video", "Chargen", "Companion Friendly", "Companions", "Compilation", "ENB Preset", "For female characters", "For male characters", "Gameplay Effects/Changes", "Official", "Performance Optimization", "Poses", "Related to horses", "Related to Movies/TV/Other Games", "Related to vampires", "Replacer", "Solstheim","none","Cheating", "Fair and balanced", "Unbalanced","BAB Bodybase", "EC/HGEC Bodybase", "Robert Female Bodybase", "Robert Male Bodybase", "TFF/UFF Bodybase"]

import csv
import numpy as np
import json

# open the file in universal line ending mode 
with open('oblivion.csv', 'rU') as infile:
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
outhead = 'Mod,Udl,time,Pop1,Pop10,Anime,LoreFriendly,NotLoreFriendly,NotSafeForWork,Nudity,SexySkimpy,Unrealistic,ArmorShields,Books,Clothing,ClothingFemale,ClothingMale,Creatures,CreaturesRideable,ItemsApparatus,ItemsClutter,ItemsFurniture,ItemsIngredients,ItemsLeveled,LocationsBuildings,LocationsCaverns,LocationsDungeons,LocationsPlayerOwned,LocationsWorldMap,MagicEnchantments,MagicPotions,MagicSpells,NPCTrainers,NPCVendors,NPCs,PlantsFoliage,Weapons,AnimationModified,AnimationNew,AudioSoundFX,AudioVoices,Birthsigns,Bodymodels,Classescomponent,EnvironmentOther,EnvironmentSky,EnvironmentWater,EnvironmentWeather,Facemodels,GuildsFactions,Hair,LeveledLists,Lighting,NewLands,Newmodels,Newtextures,Quests,RacesModified,ScriptedEvents,Video,Chargen,CompanionFriendly,Companions,Compilation,ENBPreset,Forfemalecharacters,Formalecharacters,GameplayEffectsChanges,Official,PerformanceOptimization,Poses,Relatedtohorses,RelatedtoMoviesTVOtherGames,Relatedtovampires,Replacer,Solstheim,none,Cheating,Fairandbalanced,Unbalanced,BABBodybase,ECHGECBodybase,RobertFemaleBodybase,RobertMaleBodybase,TFFUFFBodybase\n'
outl = ''

with open("../oblivion_data/taglist_o.json","r") as f:
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

with open('fit_data_o.csv','w') as f:
    f.write(outf)