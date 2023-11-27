from math import factorial
dp = 1000000001

def findzeros(n):
    count = 0
    for i in range(len(n)-1, 0, -1):
        if n[i] == '0':
            count += 1
        else:
            return count
    return count



for i in range(1, 200):
    fact = factorial(i)
    zeroes = findzeros(str(fact))      
    print("%d\t%d\t%d" %(i, 0, zeroes))      