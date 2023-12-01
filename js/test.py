import sys

input = sys.stdin.readline 

arrSize = int(input())
result = 0

for i in range(arrSize):
    if (int(input())):
        result+=1
    else:
        result-=1

print("Junhee is cute!") if (result > 0) else print("Junhee is not cute!")