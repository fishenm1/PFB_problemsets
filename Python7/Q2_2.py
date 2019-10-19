#!/usr/bin/env python3 

import re

with open("Python_07_nobody.txt","r") as poem, open ("Python_07_nicole.txt","w") as new_poem:
	for line in poem:
		line_str = str(line)
		line_sub= re.sub(r"Nobody", "Nicole", line_str)
		new_poem.write(line_sub) 

print("file written")

