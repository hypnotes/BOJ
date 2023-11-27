hanoi = []

def movetop(n, start, end):
    
    if n == 1:
        hanoi.append([start, end])
        return 
    
    movetop(n-1, start, 6-start-end)
    hanoi.append([start, end])
    movetop(n-1, 6-start-end, end)


if __name__ == "__main__":
    n = int(input())
    movetop(n, 1, 3)
    print(len(hanoi))
    for i in hanoi:
        print(i[0], i[1])