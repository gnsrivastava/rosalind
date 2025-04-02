def rna2protein(dnaString, codon_table):
	
	protein = list()
	dnaCodonList = list()

	for pos in list(range(0, len(dnaString), 3)):
		dnaCodonList.append(dnaString[pos:pos+3])
	
	start_codon_pos = dnaCodonList.index("AUG")
	
	for codonPos in range(start_codon_pos, len(dnaCodonList)):
		if dnaCodonList[codonPos] == 'UAA' or dnaCodonList[codonPos] == 'UAG' or dnaCodonList[codonPos] == 'UGA':
			break
		
		else:		
			protein.append(codon_table[dnaCodonList[codonPos]])
	
	protein = ''.join([ele for ele in protein])
	
	return protein

if __name__=='__main__':
	
	codon_table = {
		'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
		'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
		'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
		'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
		'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
		'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
		'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
		'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
		'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
		'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
		'UAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
		'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
		'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
		'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
		'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
		'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
	}

	with open('rosalind_prot.txt') as _file:
		dnaString = _file.readline().strip().rstrip()
	
	protein = rna2protein(dnaString, codon_table)
	print(protein)
