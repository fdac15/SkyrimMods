# SkyrimMods
Final Project Repository for study of Mods for Skyrim

The json files containing the information on mods from Nexus.com follow the form {mod_id : [mod_url,likes, downloads, name, description, release_date, update_date, creator, unique_downloads, pageviews]}

the json files related to the tags follow one of the following forms:
  {tag: [mod_ids_under_tag]} OR
  {mod_id: [tags_under_id]}




<b> /steam/ </b> - holds all scripts and data pretaining to the scrape of the steam workshop <br />
  Scraper file has three sections <br />
    first section - loads all of the skyrim workshop pages and records the urls directing to every mod and writes them to links.txt <br />
    second section - grabs all of the catagories and writes them to catagoroes.txt <br />
    third section - visits all of the pages in the links.txt page and visits them, creating an instance of a class and prints to a json file which was initially just output.txt <br />
    
  second file - untitled.ipynb Tag scraping -- Rename this <br />
    loads all of the tag pages and creates a dictionary of tag names keyed to mod ids prints the dictionary to a json file. <br />
  
