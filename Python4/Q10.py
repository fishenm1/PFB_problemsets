#!/usr/bin/env python3

import sys

beg = int(sys.argv[1])
end = int(sys.argv[2])+1

for value in range(beg,end):
	if value % 2 == 0:
		print(value) 
