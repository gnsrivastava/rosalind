import os, sys
from Bio import SeqIO
import operator

def gc_content(filename):
	fasta_sequences = SeqIO.parse(open(filename),'fasta')
	d = {fasta.id:round((len([l for l in str(fasta.seq) if l=="C" or l=="G"])/len(fasta))*100, 5) for fasta in fasta_sequences}
	max_keys = [key for key, value in d.items() if value == max(d.values())]
	for key in max_keys:
		return key+"\n"+str(d[key])


if __name__=="__main__":
	filename = "rosalind_gc.txt"
	gc = gc_content(filename)
	print(gc)
