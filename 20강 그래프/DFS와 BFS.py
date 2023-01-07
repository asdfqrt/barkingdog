def bfs(v):
    vis = [True] + [False]*n
    path = []
    q = deque([])
    vis[v] = True
    q.append(v)

    while q:
        cur = q.popleft()
        path.append(cur)

        for i in adj[cur]:
            if vis[i]: continue
            vis[i] = True
            q.append(i)
    return path

def dfs(cur):
    vis[cur] = True
    path.append(cur)
    for dir in adj[cur]:
        if not vis[dir]: dfs(dir)


import sys
from collections import deque
input = sys.stdin.readline

n,m,v = map(int,input().split())
adj = [[0] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

for i in range(1,n+1):
    adj[i].sort()


path = []
vis = [True] + [False]*n
dfs(v)
print(*path)
print(*bfs(v))
    
