#!/usr/bin/env python3

with open ('Python_06.seq.txt') as sequences:
	for line in sequences:
		gene_ID,seq = line.split() #splits Gene ID from sequence
		seq_lower = seq.lower() #makes sequences lowercase
		comp1 = seq_lower.replace('a','T') #next for lines create complement
		comp2 = comp1.replace('t','A')
		comp3 = comp2.replace('c','G')
		comp4 = comp3.replace('g','C')  #comp4 is the final complement
		rev_comp = comp4[::-1] #makes reverse complement 
		print(gene_ID, 'Reverse complement:', rev_comp) 	

