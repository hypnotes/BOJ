import sys 

input = sys.stdin.readline 

a, b, c = map(int, input().split())

bottles = [[a, 0], [b, 0], [c, c]]
ans = []
