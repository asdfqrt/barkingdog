import sys
from heapq import heappop, heappush

input= sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    x= int(input())
    if x: heappush(arr,x)
    else: print(heappop(arr) if arr else 0)