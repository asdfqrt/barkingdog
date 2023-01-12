# 문제 쓸데없이 복잡한데 결국 해당 노드의 자식 갯수를 찾으라는 뜻
# 아마 힌트보고 쭉 따라 써보라고 만든 문제인듯?

import sys
sys.setrecursionlimit(10**6)
input =sys.stdin.readline

n,r,q = map(int,input().split())
adj = {i:[] for i in range(1,n+1)}
for _ in range(n-1):
    a,b = map(int,input().split())
    adj[a] += [b]
    adj[b] += [a]
size = {}

def dfs(cur,p):
    size[cur]=1
    for dir in adj[cur]:
        if dir != p:
            dfs(dir,cur)
            size[cur] += size[dir]    
dfs(r,-1)

for _ in range(q):
    query = int(input())
    print(size[query])