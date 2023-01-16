import sys
from collections import deque
input= sys.stdin.readline

n,m = map(int,input().split())
adj = {i:[] for i in range(1,n+1)}
deg = [0]*(n+1)
# st = set(range(1,n+1))

for _ in range(m):
    singer = list(map(int,input().split()))
    for i in range(1,singer[0]):
        adj[singer[i]].append(singer[i+1])
        deg[singer[i+1]] +=1
#         st.discard(singer[i+1])

# q = deque(list(st))

q = deque([])
for i in range(1,n+1):
    if deg[i]==0:
        q.append(i)



result = []
while q:
    cur = q.popleft()
    result.append(cur)
    for dir in adj[cur]:
        deg[dir] -= 1
        if deg[dir] == 0:
            q.append(dir)
if len(result) ==n:
    print(*result,sep="\n")
else: print(0)