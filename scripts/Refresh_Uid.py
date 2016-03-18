import NexusScraper, time

files = ('../skyrim_data/skyrim_mods_all.json','../oblivion_data/oblivion_mods_all.json',
		 '../morrowind_data/morrowind_mods_all.json',
		 '../dragon_age_data/da2/dragon_age_2_mods_all.json',
         '../dragon_age_data/dai/dragon_age_inquisition_mods_all.json')

for file in files:
    mods = NexusScraper.json_to_modblock(file)
    i=1
    print("updating {0}".format(file))
    for mod in mods:
        time.sleep(0.1)
        print('\rgetting mod {0}/{1}'.format(i, len(mods)), end='')
        i+=1
        mod.get_pv_ud()
    
    NexusScraper.modblock_to_json(mods, file)
