#!/usr/bin/env python3

import re

gene_names = [] #emtpy list for gene names
sequences = [] # empty list for sequences
seq='' #empty string for seq

with open ("Python_08.fasta","r") as fasta:
	for line in fasta: 
		line = line.rstrip() #removes \n from end of each line 
		match = re.search(r"(^>\S+)",line) #searches for gene name format
		if match: #executes if line starts with gene name
			gene_names.append(match.group(0)) #appends gene name to gene_names list
			if seq: #executes on 2nd entry and above, appends sequence to sequences list and resets seq to empty
				sequences.append(seq)
				seq = ''
		else: 
			seq += line #accumulates sequences line
	sequences.append(seq) #appends last sequence to sequences list

# at this point, we have a list of gene names and a list of sequences

seq_codons = []

for seq in sequences:
	seq_codon = re.sub(r'(\w{3})', r'\1 ', seq) 
	seq_codons.append(seq_codon) 
	print(seq_codons) 

gene_codons_dict = dict(zip(gene_names,seq_codons))
print(gene_codons_dict) 

for gene in gene_codons_dict:
	codons = gene_codons_dict[gene] 
	print(gene, codons, sep='\t')  
