import os, sys
from scipy.special import comb

with open("rosalind_iprb.txt") as f:
	pops = f.readlines()

k,m,n = pops[0].rstrip().split(" ")
hom = int(k)
het = int(m)
rec = int(n)


pop_total = 4 * comb(hom + het + rec, 2)
dom_total = 4*comb(hom,2) + 4*hom*het + 4*hom*rec + 3*comb(het,2) + 2*het*rec
phom = dom_total/pop_total
print(phom)

