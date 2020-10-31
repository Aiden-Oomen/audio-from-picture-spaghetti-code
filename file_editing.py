import re
string = open('log.log').read()
new_str = re.sub('[,]', ' +', string)
newerstr = re.sub('[(]', '', new_str)
new_newerstr = re.sub('[)]', ' + ', newerstr)
with open('mathpy.py', 'w') as f:
	f.write(f"import replit\nggg = {new_newerstr} "[:-3])
	f.write("\nreplit.audio.play_tone(5.0, ggg, 3.0)\nprint(ggg)")
#14 lines