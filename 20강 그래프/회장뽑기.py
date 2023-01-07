# 가까운 거리 특성상 bfs써야됨

import sys
from collections import deque
input =sys.stdin.readline

n = int(input())
adj = [[0] for _ in range(n+1)]
q = deque([])

while True:
    a,b = map(int,input().split())
    if a==b==-1: break
    adj[a].append(b)
    adj[b].append(a)


def bfs(start):
    vis[start] = True
    q.append(start)
    while q:
        cur = q.popleft()
        for dir in adj[cur]:
            if vis[dir]: continue
            vis[dir] = True
            dis[dir] = dis[cur] +1
            q.append(dir)


minlvl = sys.maxsize
idx = []

for i in range(1,n+1):
    dis = [0]*(n+1)
    vis = [True] + [False] * n
    
    bfs(i)
    lvl =  max(dis)
    if lvl <= minlvl:
        if lvl < minlvl: idx=[i]
        else: idx.append(i)
        minlvl = min(lvl,minlvl)

print(minlvl,len(idx))
print(*idx)


