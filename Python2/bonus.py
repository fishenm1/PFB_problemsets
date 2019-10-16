#!/usr/bin/env python3

import sys

value = int(sys.argv[1]) #takes integer from command line as input 

print('value tested:', value) 

if value > 0:
    print ('positive') 
elif value < 0:
    print ('negative')
else: 
		print ('value equals 0')

if value % 2 == 0:
		print ('value is even')
if value % 3 == 0: 
		print ('value is divisible by 3') 
