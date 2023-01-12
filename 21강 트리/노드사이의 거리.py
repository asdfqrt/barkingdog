# 간선의 길이가 있는 트리인듯
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
adj = {i+1:[] for i in range(n)}
for _ in range(n-1):
    a,b,dis = map(int,input().split())
    adj[a] += [[b,dis]]
    adj[b] += [[a,dis]]


def dfs(cur,en,p):
    global path
    if cur==en: return True
    for dir,dis in adj[cur]:
        if dir != p:
            if dfs(dir,en,cur):
                path += dis
                return True
    return False
        



for _ in range(m):
    path = 0
    st,en = map(int,input().split())
    dfs(st,en,-1)
    print(path)


