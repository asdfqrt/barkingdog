# 노드 10^3, 간선 10^5, 노드간 간선 최대 1개
# 출발노드 1로 고정

# 반드시 지나야 하는 두 정점에서 다익스트라 돌리면 될듯?, 

import sys
from heapq import heappop, heappush

inf = float("inf")
input= sys.stdin.readline
n,e = map(int,input().split())
adj = {i:[] for i in range(1,n+1)}

for _ in range(e):
    a,b,cost = map(int,input().split())
    adj[a].append((b,cost))
    adj[b].append((a,cost))

v1,v2 = map(int,input().split())


def dijkstra(start):
    q = []
    dis = [inf]*(n+1)
    dis[start] = 0
    heappush(q,(0,start))

    while q:
        cur_dis,cur = heappop(q)
        if cur_dis != dis[cur]: continue
        for dir,cost in adj[cur]:
            if dis[dir] > dis[cur]+cost:
                dis[dir] = dis[cur]+cost
                heappush(q,(dis[dir],dir))
    return dis[1:]

dis1 = dijkstra(v1)
dis2 = dijkstra(v2)
ans = min(dis1[0] + dis2[-1], dis1[-1] + dis2[0]) + dis1[v2-1]
print(ans if ans!=inf else -1)