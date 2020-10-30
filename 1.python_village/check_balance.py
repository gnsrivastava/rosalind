'''
This is to check if brackets are balanced or not
'''
def check_balance(n):
    count1= 0
    count2= 0
    for i in range(len(n)):
        if n[i]=='[':
            count1 +=1
        elif n[i] == ']':
            count2 += 1

    if(count1 == count2):
        return(True)
    else:
        return(False)

print(check_balance("[]]"))
