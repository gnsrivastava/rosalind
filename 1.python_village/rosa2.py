with open("rosalind_ini2-3.txt", "r") as fp:
    data = fp.read().split(' ')
    a = int(data[0])
    b = int(data[1])
    if(a<1000 and b<1000):
        c = (a**2) + (b**2)
        print(c)
