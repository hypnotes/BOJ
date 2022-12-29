n = int(input())

pq = dict()
for i in range(n):
    pq[i+1]= int(input())
    

def delandAdd(b):  
    pq[1] += 1
    pq[b] -= 1


def checkwhoismax():
    cur_max = 0
    who_max = []
    for i in pq.items():
        if i[1] > cur_max:
            cur_max = i[1]
            who_max = [i[0]]
        elif i[1] == cur_max:
            who_max.append(i[0])
            
    return who_max


count = 0
b = [-1]

while  b[0] != 1 or len(b) != 1 :

    b = checkwhoismax()
    blen = len(b)
    
    if blen == 1 and b[0] == 1:
        print(count)
        break
    
    if b[0] == 1 and blen!= 1:
        delandAdd(b[1])
    else:
        delandAdd(b[0])
    count+=1
    
