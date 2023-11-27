
a, b = map(int, input().split())

q = [x for x in range(1, 1+a)]
rear = 0

while(len(q)!=0):
    rear+=(b-1)
    while rear >= len(q):
        rear=rear-len(q)
    
    print(q[rear])
    del(q[rear])
    
    


            
            
