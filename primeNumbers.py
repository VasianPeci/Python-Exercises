def isPrime(n):
    if (n==0 or n==1):
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
N=100
for i in range (1,N+1):
    if isPrime(i):
        print(str(i)+' ')
