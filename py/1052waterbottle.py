n, k = map(int, input().split())

buy = 0


while True:
    
    binN = bin(n)[2:]
    bottles = 0
    
    for i in range(len(binN)):
        if binN[i] == '1':
            bottles+=1
    
    if bottles <= k:
        print(buy)
        break
    
    n+=1
    buy+=1