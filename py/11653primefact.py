
n = int(input())

#p = [0] * (n+1)

def checkPrime(a):
    
    if a == 4:
        return 0
    for i in range(2, a//2):
        if a%i == 0:
            return 0
    return 1


if n == 1:
    pass
elif n == 4:
    print("%d\n%d" %(2, 2))
elif checkPrime(n):
    print(n)
else:
    for i in range(2, n//2):
        if checkPrime(i):
            while n % i == 0:
                n //= i
                print(i)
                if n == i:
                    break
            if checkPrime(n):
                print(n)
                break
    