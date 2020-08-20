from math import sqrt

##judge if n is an prime
def isPrime(n):
    for i in range(2,int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


lower = int(input())
upper = int(input())
num=[]
for i in range(lower,upper+1):
    if i == 2:
        num.append(i)
    if i > 2 and isPrime(i):
        num.append(i)
print(num)
