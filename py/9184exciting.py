di = {}

for i in range(21):
    for j in range(21):
        for k in range(21):
            di["%d %d %d" %(i,j,k)]=0

# for i in di:
#     print(i)
    
def inrange(n):
    return n>0 and n<21

def w(a, b, c):
    
    if inrange(a) and inrange(b) and inrange(c) and di["%d %d %d" %(a,b,c)]:    #이미 존재하면
        return di["%d %d %d" %(a,b,c)]
    
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    
    elif a > 20 or b > 20 or c > 20:
        di["%d %d %d" %(a,b,c)] = w(20, 20, 20)
        return di["%d %d %d" %(a,b,c)] 
    
    elif a < b and b < c:  # a < b < c
        di["%d %d %d" %(a,b,c)]= w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return   di["%d %d %d" %(a,b,c)]
   
    else:
        di["%d %d %d" %(a,b,c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return di["%d %d %d" %(a,b,c)]


    
while True:
    a, b, c = map(int, input().split())
    if a==-1 and b==-1 and c==-1:
        break
    print("w(%d, %d, %d) = %d" %(a,b,c, w(a,b,c)))
    