# a = int(input())

a = 3
b = a//3 
k = 0

while b != 1:
    b/=2 
    k+=1

print("%d = 3 x 2^%d" %(a, k))

space = a-1 

stars = ['*', '* *', '*****']

for i in range(10):
    print(i, "3 mod %d = %d " %(i+1, 3%(i+1)))
    print((space)*' '+stars[3%(i+1)])
    space -=1