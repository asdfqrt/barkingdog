import sys
from heapq import heappush, heappop

input = sys.stdin.readline
v,e = map(int,input().split())
k = int(input())
heap = []
dis = [float("inf")]*(v+1)
adj = [[]*(v+1) for _ in range(v+1)]
for _ in range(e):
    a,b,cost = map(int,input().split())
    adj[a].append((b,cost)) #튜플이 리스트보다 더 빠름

dis[k] = 0
heappush(heap,(0,k))

while heap:
    cur_dis, cur = heappop(heap)
    if dis[cur] != cur_dis: continue
    for dir,cost in adj[cur]:
        if dis[dir] > dis[cur]+cost:
            dis[dir] = dis[cur]+cost
            heappush(heap,(dis[dir],dir))

for i in dis[1:]:
    print(i if i!=float("inf") else "INF")