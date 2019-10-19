#!/usr/bin/env python3

import re

gene_names = [] #emtpy list for gene names
sequences = [] # empty list for sequences
seq='' #empty string for seq

with open ("Q1.test.txt","r") as fasta:
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

print(gene_names)
print(sequences) 
# at this point, we have a list of gene names and a list of sequences

# now we will create a list of nucleotide counts dictionaries

nt_count= [] #creates empty list 

for sequence in sequences: #this section populates count values in dictionaries
	count = {} 
	count['A'] = sequence.count('A')
	count['T'] = sequence.count('T')
	count['G'] = sequence.count('G')
	count['C'] = sequence.count('C') 
	nt_count.append(count) 
	
print (nt_count) #this is a list of dictionaries

#create a dictionary of gene names and nt counts

gene_nt_dict = dict(zip(gene_names,nt_count))
print (gene_nt_dict)

for gene in gene_nt_dict:
	output = [gene]
	for nucleotide in gene_nt_dict[gene]:
		count= gene_nt_dict[gene][nucleotide]
		output.append(count) 
	print(output)

for line in output: 
	print(line, "\t")

