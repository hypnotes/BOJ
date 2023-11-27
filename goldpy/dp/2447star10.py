from operator import indexOf

n = [ 3**i for i in range(0, 9)]
n = indexOf(n, int(input()))

past = ['***', '* *', '***']
        
def drawstar(m, past):
    
    if m == n:
        for i in past:
            print(i)
        return
    
    plen = len(past[0])
    newdraw = [i*3 for i in past]
    middle = []
    
    for i in past:
        middle.append(i + (" " * plen) + i)
    
    newdraw.extend(middle)
    
    for i in range(plen):
        newdraw.append(newdraw[i])
    
    past = newdraw
    
    drawstar(m+1, past)
                
drawstar(1, past)