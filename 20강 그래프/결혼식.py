import sys
from collections import deque
input =sys.stdin.readline

n = int(input())
m = int(input())
vis = [True] + [False] * n
adj = [[0] for _ in range(n+1)]
dis = [0]*(n+1)

for _ in range(m):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

q = deque([])
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

bfs(1)
cnt = 0
for i in dis:
    if 0<i<3: cnt+=1
print(cnt)

