import os, sys
from Bio import SeqIO


with open("rosalind_hamm.txt") as f:
	fastas = f.readlines()
d = {fastas[0].rstrip():[line.rstrip() for line in fastas if line != fastas[0]]}
for ref_seq, seqs in d.items():
	result = [sum(b1 != b2 for b1, b2 in zip(ref_seq, seq)) for seq in seqs]
	if len(result) == 1:
		print(result[0])
	else:
		print(result)

