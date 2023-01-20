#1초, 노드 10^3, 간선 10^5
#노드 1000개면 플로이드 알고리즘은 시간 모자랄수있음, 출발지 1개>> 다익스트라 ㄱ


import sys
from heapq import heappop, heappush

input= sys.stdin.readline

n = int(input())
m = int(input())
adj = [[]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,cost = map(int,input().split())
    adj[a].append((b,cost))
st,en = map(int,input().split())


dis = [float('inf')]*(n+1)
pre = [-1]*(n+1)
dis[st] = 0

q = []
heappush(q,(0,st))

while q:
    cur_dis, cur = heappop(q)
    if dis[cur] != cur_dis: continue
    for dir,cost in adj[cur]:
        if dis[dir] > dis[cur]+cost:
            dis[dir] = dis[cur]+cost
            pre[dir] = cur
            heappush(q,(dis[dir],dir))
path = []
cur = en
while cur != st:
    path.append(cur)
    cur = pre[cur]
path.append(st)

print(dis[en])
print(len(path))
print(*reversed(path))


