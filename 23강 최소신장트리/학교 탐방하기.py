#최적경로와 최악경로 둘다 구해야됨
#mst랑 간선 value -로 해서 mst돌린거 두번 구하면 될듯?
#정렬시 cost가 최하인것, 최상인것 
# 0에서 1로 가는거 있음 >>vis==n까지
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
for _ in range(m+1):
    a,b,cost = map(int,input().split())
    edge.append([cost,a,b])
edge.sort()


min_ans =0
max_ans =0
vis =0
for cost,a,b in edge:
    if union(a,b): continue
    max_ans +=1 if cost==0 else 0
    vis +=1
    if vis==n: break

vis =0
p = [i for i in range(n+1)] #p초기화 해줘야됨
for cost,a,b in reversed(edge):
    if union(a,b): continue
    min_ans +=1 if cost==0 else 0
    vis +=1
    if vis==n: break

print(max_ans**2 - min_ans**2)