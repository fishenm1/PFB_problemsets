#!/usr/bin/env python3

list_headers = []
list_seq = []
seq = ''

with open ('Q5.fasta','r') as file:  
	for line in file: 
		line = line.rstrip()
		if line.startswith('>'):
			list_headers.append(line)
			if seq: 
				list_seq.append(seq)
				seq = ''
		else:
			seq += line
	list_seq.append(seq) 			

print (list_headers)
print (list_seq) 

fastaDict= dict(zip(list_headers,list_seq))
print('My New Dictionary:',fastaDict)


