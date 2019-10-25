#!/usr/bin/env python3

import sys

bamfile = sys.argv[1] #second item on command line is a bam file  
gene_read_counter = {} #creates empty dictionary 

with open(bamfile, 'r') as file: #opens bam file 
    for line in file:  
        line = line.rstrip() #takes off line breaks at end  
        fields = line.split('\t') #splits each line into a list, with item being a different column 
        gene_transcript = fields[2] #column 3 is gene/transcript name 
        read = fields[0] #column 1 is read name
        (gene_name, transcript_name) = gene_transcript.split('^') #column 3 is formatted as gene name ^ transcript, so this splits that into two variables
        if gene_name in gene_read_counter: #adds additional reads to sets in dictionary; empty set is created in the "else" section below 
            read_set = gene_read_counter[gene_name] 
            read_set.add(read) 
        else: #gene_names will go here first! creates a key for gene_name and an empty set as value 
            gene_read_counter[gene_name] = set() 
            gene_read_counter[gene_name].add(read)  

#generate report 

for gene_name in sorted(gene_read_counter, key = lambda x: len(gene_read_counter[x]), reverse=True):  #sorts by length of set
    read_set = gene_read_counter[gene_name] #sets variable for set
    num_reads = len(read_set) #calculates the number of unique reads for each set 
    print("\t".join([gene_name, str(num_reads)])) #prints gene name and number of unique reads in order from highest to lowest


