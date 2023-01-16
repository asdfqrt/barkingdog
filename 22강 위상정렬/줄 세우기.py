import sys
from collections import deque
input= sys.stdin.readline

n,m = map(int,input().split())
adj = {i+1:[] for i in range(n)}
deg = {i+1:0 for i in range(n)}
q = deque([])

for i in range(m):
    a,b = map(int,input().split())
    adj[a].append(b)
    deg[b] += 1

for i in range(1,n+1):
    if deg[i] == 0:
        q.append(i)

result = []
while q:
    cur = q.popleft()
    result.append(cur)
    for dir in adj[cur]:
        deg[dir] -= 1
        if deg[dir] == 0:
            q.append(dir)

print(*result)
