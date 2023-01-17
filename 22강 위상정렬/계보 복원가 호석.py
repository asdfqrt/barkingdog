# 자식갯수 > 직속자식만이이니까 bfs 하는 도중에 별도 리스트에 추가 
#
import sys
from collections import deque, defaultdict

input= sys.stdin.readline

n = int(input())
name = input().split()
name.sort()
m = int(input())

adj = {i:[] for i in name}
deg = defaultdict(int)
child = defaultdict(list)

for _ in range(m):
    son,anc = input().split()
    adj[anc].append(son)
    deg[son] += 1

q = deque([])
for ppl in name:
    if ppl not in deg:
        q.append(ppl)
print(len(q))
print(*q)

while q:
    cur = q.popleft()
    for dir in adj[cur]:
        deg[dir] -= 1
        if deg[dir] == 0:
            child[cur].append(dir)
            q.append(dir)

for name in name:
    print(name,len(child[name]),*sorted(child[name]))
