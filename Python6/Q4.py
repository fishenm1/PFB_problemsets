#!/usr/bin/env python3

line_count = 0 #sets line count variable
total_characters = 0 #sets character count variable

with open ('Python_06.seq.txt') as file:
	for line in file:
		line_count += 1 #adds a count for each line that goes through loo
		line_strip = line.rstrip() #gets rid of \n so they aren't included in line count
		num_characters = len(line_strip) #number of characters in each line 
		total_characters += num_characters #adds count to characters

print("Total number of lines:", line_count) 
print("Total number of characters:", total_characters)

avg_line_length = int(total_characters/line_count)
print("Average line length:", avg_line_length)

