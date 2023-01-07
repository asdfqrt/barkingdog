import sys
input =sys.stdin.readline

n = int(input())
m = int(input())
vis = [True] + [False] * n
adj = [[0] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

cnt = 0
def dfs(cur):
    global cnt
    vis[cur] = True
    cnt += 1
    for dir in adj[cur]:
        if not vis[dir]: dfs(dir)

dfs(1)
print(cnt-1)