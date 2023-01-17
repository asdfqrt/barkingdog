def find(cur):
    if p[cur]==cur: return cur
    p[cur] = find(p[cur])
    return p[cur]

def Union(a,b):
    a=find(a)
    b=find(b)
    if a==b: return True
    else:
        if a<b: p[b] = a
        else: p[a] = b
        return False
import sys

input = sys.stdin.readline
v,e = map(int,input().split())
p = [i for i in range(v+1)]
edge = []

for _ in range(e):
    a,b,cost = map(int,input().split())
    edge.append([cost,a,b])
edge.sort()

cnt = 0
ans = 0
for cost,a,b in edge:
    if Union(a,b): continue
    ans += cost
    cnt +=1
    if cnt == v-1: break

print(ans)
