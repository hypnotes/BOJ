
from operator import indexOf


def selfnum(num):
    val = num 
    while num >0:
        val += (val%10)
        num //= 10

    return val
        
        
    
li = [0] * 10001
for i in range(10000):
    nonselfnum = selfnum(i)
    if nonselfnum < 10001:
        li[nonselfnum] = 1

for i in range(len(li)):
    if li[i]:
        print(i)
    
    
