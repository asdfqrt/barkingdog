#최소 스패닝 트리 문제
def find(cur):
    if p[cur]==cur: return cur
    p[cur]= find(p[cur])    #이거넣으니까 되던데 이게 어째서 시간을 줄여주지??? >> anc가 기록됨, union에 의해 햡쳐졌을 수 있는 anc의 조상을 한번더 체크할 뿐
    return p[cur]
def union(a,b):
    anc_a = find(a)
    anc_b = find(b)
    if anc_a==anc_b: return True
    if anc_a<anc_b: p[anc_b] = anc_a
    else: p[anc_a] = anc_b
    return False

import sys
sys.setrecursionlimit(10**6)
# from heapq import heappop, heappush
input= sys.stdin.readline

n = int(input())
edge = []
p = [i for i in range(n+1)]
for i in range(n):
    cost = map(int,input().split())
    for j,cost in enumerate(cost):
        if j<=i: continue
        # heappush(edge,[cost,i+1,j+1])
        edge.append([cost,i+1,j+1])
edge.sort()

ans = 0
vis = 0
for cost,i,j in edge:
# while edge:
#     cost,i,j = heappop(edge)    
    if union(i,j): continue
    ans +=cost
    vis +=1
    if vis==n-1: break

print(ans)

#힙보다 sort하는게 더 빠른데?? 힙 push pop > 각각logn이므로 총 n개에 다하면 2nlogn
#append n + sort하면 nlogn + 한개씩 사용할때 n>> n+nlogn+n인가