
#큐로 하면 안될듯
#일반 배열로 하고 팝할때마다 min value를 빼는걸로
# min value만 특정해서 빼기에 최적화된 힙 쓰면 될듯?

import sys
from heapq import heappop, heappush


input = sys.stdin.readline
n,m = map(int,input().split())
adj = {i:[] for i in range(1,n+1)}
deg = [0]*(n+1)
heap = []

for _ in range(m):
    st,en = map(int,input().split())
    adj[st].append(en)
    deg[en] += 1


for prob in range(1,n+1):
    if deg[prob] == 0:
        heappush(heap,prob)
while heap:
    cur = heappop(heap)
    print(cur,end=" ")
    for dir in adj[cur]:
        deg[dir] -= 1
        if deg[dir] ==0:
            heappush(heap,dir)



