#!/usr/bin/env python3

import sys

value = int( sys.argv[1]) #assigns value to integer of sys.argv[1] input

if value > 0:
	print('positive') #print positive if input is positive
	if value <50: #adds nested test to see if value is less than 50 
		print ('smaller than 50') 
		if value % 2 == 0: #adds nested test to see if value is even 
			print ('value is even')
		if value <50 and value % 2 ==0: 
			print('it is an even number that is smaller than 50')
	else: 
		print('larger than 50') #prints that value is larger than 50
		if value % 3 ==0: #nested test- is number divisible by 3?
			print ('it is larger than 50 and divisible by 3') 
elif value < 0:
	print('negative') #print negative if input is negative
else:
	print('value equals 0') #if value equals 0


