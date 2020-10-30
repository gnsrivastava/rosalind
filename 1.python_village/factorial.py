# This is to find factorial of a given number n =5
# Users can either enter a number in the code or ask program to ask for an input. 
#Depends on what yu prefer

def factorial(n):
    fac = 1
    if(n<0):
        return(-1)
    elif(n==0 or n==1):
        return(1)
    else:
        for i in range(1,n+1):
            fac = fac*i
        return(fac)

print(factorial(5))
