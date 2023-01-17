# def find(cur):
#     if p[cur] == cur: return cur
#     # p[cur] = find(p[cur]) #p[cur]을 기록을 혹시나 하더라도 매 find 마다 적혀있는 p[cur]과 무관하게 다 탐색하는데 굳이 매회 수정할 필요가 있나?
#     return find(p[cur])
# def union(a,b):
#     anc_a = find(a)
#     anc_b = find(b)
#     if anc_a == anc_b: return True
#     else:
#         if anc_a < anc_b: p[anc_b] = a
#         else: p[anc_a] = b

# import sys
# input= sys.stdin.readline

# n = int(input())
# edge = []
# p = [i for i in range(n+2)] # 마지막에 관념노드 한개까지 추가


# for i in range(n):
#     cost = int(input())
#     edge.append([cost,i+1,n+1])
# for i in range(1,n+1):
#     cost = map(int,input().split())
#     for j,cost in enumerate(cost):
#         if cost==0: continue
#         edge.append([cost,i,j+1])
# edge.sort()

# ans = 0
# cnt = 0
# for cost,i,j in edge:
#     if union(i,j): continue
#     ans +=cost
#     cnt +=1
#     if cnt == n: break
# print(ans)

#####################################
#힙을 사용하면 sort없이 사용가능
def find(cur):
    if p[cur] == cur: return cur
    p[cur] = find(p[cur]) #p[cur]을 기록을 혹시나 하더라도 매 find 마다 적혀있는 p[cur]과 무관하게 다 탐색하는데 굳이 매회 수정할 필요가 있나?
    return p[cur]
def union(a,b):
    anc_a = find(a)
    anc_b = find(b)
    if anc_a == anc_b: return True
    else:
        if anc_a < anc_b: p[anc_b] = a
        else: p[anc_a] = b


import sys
from heapq import heappop, heappush
input= sys.stdin.readline

n = int(input())
edge = []
p = [i for i in range(n+2)] # 마지막에 관념노드 한개까지 추가


for i in range(n):
    cost = int(input())
    heappush(edge,[cost,i+1,n+1])
for i in range(1,n+1):
    cost = map(int,input().split())
    for j,cost in enumerate(cost):
        if cost==0: continue
        heappush(edge,[cost,i,j+1])

ans = 0
cnt = 0
while cnt<n:
    cost,i,j = heappop(edge)
    if union(i,j): continue
    ans +=cost
    cnt +=1
print(ans)