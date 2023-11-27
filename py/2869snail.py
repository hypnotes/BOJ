
from math import ceil

a, b, v = map(int, input().split())

c = a -b

print(ceil((v-a)/(a-b))+1)
    
     