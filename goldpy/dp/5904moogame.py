n = int(input())

m, ans, i  = 3, 0, 1
a, b = m, m+i+3
m = 2*m + i+3

while n > m:
    i+=1
    a= m #index
    b =  a+i+3
    m = 2*m + i+3   #length
   
while True:

    if (n >a and n <= b):
        print("m") if n==a+1 else print("o")
        break
    else: 
        if n > b:
            n = n-a-(i+3)
        
        m = a
        a= (m-(b-a-1))//2
        b = a+i+2
        i -= 1
            
