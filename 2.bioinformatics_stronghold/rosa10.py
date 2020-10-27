
n = int(input("Enter number of months: "))
k = int(input("Enter number of pairs: "))
val = [0] * (n)

def rabbits(n):
    if n == 1 or n == 2:
        return 1
    elif val[n-1] != 0:
        return val[n-1]
    else:
        val[n-2] = rabbits(n-1)
        return rabbits(n-1) + k * rabbits(n-2)

rabbit_pairs = rabbits(n)
print(rabbit_pairs)