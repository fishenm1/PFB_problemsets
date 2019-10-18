#!/usr/bin/env python3 

#open and read file python06.txt, uppercase each line, and print out eachto the STDOUT

with open ("python06.txt", "r") as file, open ("Python_06.seq.txt", "w") as output_file:
	for line in file: 
		line_upper = line.upper()
		line_strip = line_upper.rstrip()
		output_file.write(line_strip + "\n")
	print ('output file written')
