with open("rosalind_ini5.txt", "r") as fp:
    data = fp.read().splitlines()
    lines = [data[i] for i in range(1,len(data), 2)]
    for i in range(0,len(lines)):
        print(lines[i])