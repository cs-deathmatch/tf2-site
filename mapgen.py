# check the map prefix
# if cp_, cross reference with list of a/d maps
# otherwise, just use the prefix to write the gamemode directly

# dictionary:
# %filename%
# %gamemode%
# %plainname%

import re

# load template text. i can just hardcode that its fine this is python
html = '<div class="mapbox"> <img width="270" src="/assets/mapimages/live/%filename%.jpg" alt="%filename%"> <div class="mapname"> <img title="%gamemode%" width="30px" height="30px" style="margin-top: 1.4em;margin-right: 0.5em;" src="/assets/%gamemode%.png" alt="%gamemode%"> <p>%plainname%</p></div></div>'

# prompt for user to enter list of mapnames to process in console. space separated.
print("Enter list of maps (space separated):")
worklist = input()

# generate array
splitlist = worklist.split()

# insert the map name into the relevant spots

for entry in splitlist:
    stage1 = html.replace("%filename%", entry)

    # grab everything before the first underscore (ctf_2fort -> ctf)
    match = re.match(r'^[^_]*', entry)
    prefix = match.group(0)

    stage2 = stage1.replace("%gamemode%", prefix)
    match2 = re.search(r'(?<=_).*', entry)
    mapname = match2.group(0)
    capname = mapname.capitalize()

    stage3 = stage2.replace("%plainname%", capname)
    print(stage3)