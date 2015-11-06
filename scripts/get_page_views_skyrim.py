import NexusScraper

mods = NexusScraper.json_to_modblock('skyrim_mods_all.json')

NexusScraper.pageviews_to_json(mods, start=0, end=len(mods), name='skyrim_pageviews_all.json', verbose=True)
