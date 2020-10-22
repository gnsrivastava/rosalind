with open("rosalind_rna-2.txt", "r") as fp:
    s = fp.readline()
    x = s.replace('T', 'U') # this is to replace a string without going to loop
    print(x)

