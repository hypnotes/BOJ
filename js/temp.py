import sys
input = sys.stdin.readline

n, h = map(int, input().split(" "))
bottomArr = []
topArr = []
for i in range(n):
    t = int(input())
    if(i%2):
        topArr.append(t)
    else:
        bottomArr.append(t)


def binarySearch(arr, finding, left, right):
    while left < right:
        mid = int((left+right)//2)

        if(arr[mid]>=finding):
            right = mid
        else:
            left = mid + 1
    
    return len(arr)-right

topArr.sort()
bottomArr.sort()
ans, ansCount= n, 0


for i in range(1, h+1):
    totalBreak = binarySearch(topArr, h-i+1, 0, n/2) + binarySearch(bottomArr, i, 0, n/2)

    if (totalBreak == ans):
      ansCount+=1
      continue

    if(ans > totalBreak):
      ans = totalBreak
      ansCount=1
    
print(int(ans), ansCount)
