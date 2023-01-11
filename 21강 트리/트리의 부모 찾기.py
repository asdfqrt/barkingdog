#dfs
import sys
input= sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(cur):
    for nxt in adj[cur]:
        if p[cur]!=nxt:
            p[nxt] = cur
            dfs(nxt)
n = int(input())
adj = [[] for _ in range(n+1)]
p = [0]*(n+1)
for i in range(n-1):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
dfs(1)

print(*p[2:], sep="\n")



########################
#bfs
import sys
from collections import deque
input= sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n+1)]
p = [0]*(n+1)
for i in range(n-1):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

q = deque([1])
while q:
    cur = q.popleft()
    for dir in adj[cur]:
        if p[cur] != dir:
            p[dir] = cur
            q.append(dir)

print(*p[2:], sep="\n")