
with open("rosalind_ini4-2.txt", "r") as fp:
    data = fp.read().split()
    a = int(data[0])
    b = int(data[1])
    odds = [x for x in range(a,b+1) if x%2==1]
    print(sum(odds))
        