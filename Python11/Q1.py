#!/usr/bin/env Python3

#create a DNA sequence class that will contain a sequence, its name, and it's organism of origin. Do this by creating an _init_function. 

class DNAsequence(object):
	#define class attributes
	def  __init__(self, sequence, gene_name, species_name):
		self.sequence = sequence
		self.gene_name = gene_name
		self.species_name = species_name
	#define methonds
	def seq_len(self):
		length = len(self.sequence)
		return length 	
	def nt_comp(self):
		A_count = self.sequence.count('A')
		T_count = self.sequence.count('T')
		G_count = self.sequence.count('G')
		C_count = self.sequence.count('C')
		nt_comp = 'A:'+str(A_count), 'T:'+ str(T_count), 'G:'+str(G_count), 'C:'+str(C_count)   
		return  nt_comp 
	def gc_content(self):
		G_count = self.sequence.count('C')
		C_count = self.sequence.count('G')
		GC_count = G_count + C_count 
		GC_fraction = GC_count / self.seq_len() 
		return GC_fraction
	def fasta(self): 
		fasta  = '>' + self.gene_name + '\n' + self.sequence	 
		return fasta
#Write some some lines of code, outside your class (in your main program) that sets the name, DNA sequence, and organism for a gene.

DNAseq_object1 = DNAsequence('ATCGA','GENE1','Homo sapiens') 

#Write some some lines of code, outside your class that:
#a. uses the object sequence attribute to retrieve and print the sequence.
#b. uses the object name attribute to retrieve and print the name.
#c. uses the object organism attribute to retrieve and print the organism.

print('Sequence:',DNAseq_object1.sequence) 
print('Name:', DNAseq_object1.gene_name)
print('Organism:', DNAseq_object1.species_name) 

print ('Seq Length:', DNAseq_object1.seq_len())

print ("NT comp:",DNAseq_object1.nt_comp())

print ("GC content:", DNAseq_object1.gc_content())

print (DNAseq_object1.fasta()) 
