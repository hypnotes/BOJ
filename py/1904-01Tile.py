n = int(input())

if n < 3:
    print(n)
else:
    a = 1
    b = 2
    for i in range(3, n+1):
        a, b = b, (a+b )%15746

    print(b)


# while True:
#     n = int(input())
    
#     for i in range(pow(2, n)):
#         newi = bin(i)[2:]
#         if len(newi) != n:
#             newi = '0'*(n-len(newi))+newi
#         print(newi)
