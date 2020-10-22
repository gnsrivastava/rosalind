with open("rosalind_ini3-2.txt", "r") as fp:
    data = fp.read().splitlines()
    string = str(data[0])
    num = data[1].split(' ')
    a = int(num[0])
    b = int(num[1])
    c = int(num[2])
    d = int(num[3])
    print(string[a:b+1], string[c:d+1])