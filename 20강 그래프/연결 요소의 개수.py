import sys
from collections import deque
input= sys.stdin.readline

n,m = map(int,input().split())

adj = [[0] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)
##########################################
#bfs
#leftpop만 pop으로 바꾸면 dfs

def bfs(n):     #bfs(n,adj)할필요 없는게 adj는 어짜피 리스트라 함수안에서 밖으로 접근가능
    q = deque([])
    vis = [True] + [False]*n
    cnt = 0
    for i in range(1,n+1):
        if vis[i]: continue
        vis[i] = True
        q.append(i)
        cnt += 1

        while q:
            cur = q.popleft()
            for dir in adj[cur]:
                if vis[dir]: continue
                vis[dir] = True
                q.append(dir)
    return cnt
# print(bfs(n))
########################################
#재귀 dfs

sys.setrecursionlimit(10 ** 4) # 백준에 재귀 깊이제한이 있어서 늘려줘야됨
vis = [True] + [False]*n
cnt = 0

def dfs(cur):
    vis[cur] = True
    for dir in adj[cur]:
        if not vis[dir]: dfs(dir)
  
        
for i in range(1,n+1):
    if vis[i]: continue
    cnt +=1
    dfs(i)
print(cnt)
#######################################



