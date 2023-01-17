# 그냥 mst한 다음에 유지비 제일큰 간선 하나 빼내면 트리 2개로 나눠짐
def find(cur):
    if p[cur]==cur: return cur
    p[cur] = find(p[cur])
    return p[cur]
def union(a,b):
    anc_a = find(a)
    anc_b = find(b)
    if anc_a==anc_b: return True
    if anc_a<anc_b: p[anc_b] = anc_a
    else: p[anc_a] = anc_b

import sys
sys.setrecursionlimit(10**6)
input= sys.stdin.readline


n,m = map(int,input().split())
edge = []
p = [i for i in range(n+1)]
for _ in range(m):
    a,b,cost = map(int,input().split())
    edge.append([cost,a,b])
edge.sort()

ans =0
vis =0
max_cost = 0
for cost,a,b in edge:
    if union(a,b): continue
    max_cost = max(max_cost,cost)
    ans +=cost
    vis +=1
    if vis==n-1: break
print(ans-max_cost)
