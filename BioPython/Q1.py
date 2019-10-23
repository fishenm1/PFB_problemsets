#!/usr/bin/env python3

from Bio import SeqIO

for seq_record in SeqIO.parse('Python_07.fasta', 'fasta'):
	print ('ID',seq_record.id)
	print('Sequence',seq_record.seq) 
	print('Length',len(seq_record)) 


	
