import re 
from re import finditer 

def NumberofCounts(s):
	count = []

	for nt in ['A', 'T', 'G', 'C']:
		count.append(len([match.start()+1 for match in finditer(f'(?={nt})', s)]))
	
	return count  


if __name__ == '__main__':
	
	with open('rosalind_ini.txt') as _file:
		data = _file.readline().strip()

	count = NumberofCounts(data)
	print(' '.join([str(cnt) for cnt in count]))

