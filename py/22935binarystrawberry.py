t = int(input())

for _ in range(t):        
        
    n = int(input())
    modn = n%28
    if modn > 15:
        modn = 30-modn
    elif modn == 0:
        modn = 2
        
    newn = bin(modn)[2:]
    zeroneeded = 4-len(newn)
    
    ans = 'V'*zeroneeded
    for i in range(len(newn)):

        if newn[i] == '0':
            ans += 'V'
        else:
            ans += '딸기'
    print(ans)