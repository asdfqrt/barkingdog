# MST인데 선택해야되는 간선몇개가 정해져 있는듯 >> 배열의 최 앞단에 dis 0으로 넣어서 미리 고려하도록 하면되지
# 기존의 배열을 사용하지 않고 새로 파는게 이득일수도?> 그럴일은 없을듯??
# 매 간선의 길이가 주어지지 않는데 그러면 두 좌표사이의 모든 거리 다 계산해서 직접 edge에 넣어야되는듯?
def distance(a,b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**(0.5)

def find(cur):
    if p[cur]==cur: return cur
    p[cur]=find(p[cur])
    return p[cur]

def union(a,b):
    anc_a = find(a)
    anc_b = find(b)
    if anc_a==anc_b: return True
    if anc_a<anc_b: p[anc_b]=anc_a
    else: p[anc_a]=anc_b

import sys
input= sys.stdin.readline


n,m = map(int,input().split())
arr = [[]]
p=[i for i in range(n+1)]
for _ in range(n):
    x,y = map(int,input().split())
    arr.append([x,y])

checklist = set()
for _ in range(m):
    a,b = map(int,input().split())
    checklist.add((a,b))

edge = []
for i in range(1,n+1):
    for j in range(1,i):
        if (i,j) in checklist or (j,i) in checklist:
            edge.append([0,i,j])
            continue
        edge.append([distance(arr[i],arr[j]),i,j])
edge.sort()

ans = 0
vis = 0
for cost,i,j in edge:
    if union(i,j): continue
    ans += cost
    vis +=1
    if vis==n-1: break
print("{:.2f}".format(ans))
