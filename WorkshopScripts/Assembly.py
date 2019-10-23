#!/usr/bin/env python3

contig_count = 0
current_contig = ''
contigs_list=[]

with open ('ecoli_0.25.contigs.fasta', 'r') as fasta: 
	for line in fasta:
		line = line.rstrip()
		if line.startswith('>'):
			if current_contig:
				contigs_list.append (current_contig)
				contig_count += 1 
				current_contig = ''
		else:
			current_contig += line 

print ('Number of contigs:',contig_count)

contigs_sorted = sorted(contigs_list, key=len, reverse=True) 

genome_size = sum(len(contig) for contig in contigs_sorted) 
print ('Genome size:' ,genome_size) 
			
print ('Longest contig length:', len(contigs_sorted[0]))
print ('Shortest contig length:', len(contigs_sorted[-1]))
	
#identify contig for L50 and N50 

half_mark = genome_size / 2
N50 = 0
count = 0

for contig in contigs_sorted:
	while count < half_mark:
		count += len(contig)
		N50 += 1

L50  = len(contigs_sorted[N50])
print ('half_mark:', half_mark)
print ('Count:',count) 
print('N50:', N50)
print('L50:', L50) 
print ('Length contig 10:', len(contigs_sorted[10]))


 





			

