#!/usr/bin/env python3

mylist = [101,2,15,22,95,33,2,27,72,15,52]

sorted_list= sorted(mylist)  #sort list above
print(sorted_list) #print sorted list

even_sum = 0 #sets even sum variable to add to in loop
odd_sum = 0 #sets odd sum variable to add to in loop
	
for value in sorted_list: # start loop
	print(value)
	if value % 2 == 0: #identifies even values
		even_sum += value 
	else: #odd values go here
		odd_sum += value 

print('Sum of even numbers:',even_sum)
print('Sum of odd numbers:',odd_sum)

