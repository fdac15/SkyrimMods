import NexusScraper

oblivionMods = NexusScraper.get_nexus_mods_from_pages(site='oblivion', verbose=True, rr=0.1,start=1,end=880)

NexusScraper.modblock_to_json(oblivionMods, name='oblivion_mods_all.json')

morrowindMods = NexusScraper.get_nexus_mods_from_pages(site='morrowind', verbose=True, rr=0.1,start=1,end=119)

NexusScraper.modblock_to_json(morrowindMods, name='morrowind_mods_all.json')
