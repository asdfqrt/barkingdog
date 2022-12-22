import sys
from collections import deque

N,M = map(int,input().split())
num = list(map(int,sys.stdin.readline().rstrip().split()))
list = deque(range(1,N+1))
cnt = 0

for i in range(len(num)):
    if list.index(num[i])+1 > (len(list)/2)+1:
        while list[0] != num[i]:
            list.rotate(1)
            cnt += 1
    else:
        while list[0] != num[i]:
            list.rotate(-1)
            cnt += 1
    list.popleft()
print(cnt)
