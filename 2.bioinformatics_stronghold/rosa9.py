with open("rosalind_revc.txt", "r") as fp:
    s = fp.readline()
    s = s.replace('A', 't')
    s = s.replace('C', 'g')
    s = s.replace('G', 'c')
    s = s.replace('T', 'a') 
    sc = s.upper()[::-1] 
    print(sc)     
