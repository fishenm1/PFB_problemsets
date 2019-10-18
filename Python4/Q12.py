#!/usr/bin/env python3

sequences = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

seq_tuples = (len(seq)\tseq for seq in sequences)

for tuple in seq_tuples:
	print(tuple)

