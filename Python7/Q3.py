#!/usr/bin/env python3

import re

with open ("Python_07.fasta", "r") as fasta:
		for line in fasta:
			line = line.rstrip()
			match = re.search(r"(^>\S+\s+.+)",line)
			if match:
				print (match.group(1))


