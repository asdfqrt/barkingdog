# 플로이드 말고 그냥 dfs돌려도 되겠는데?
# 사이클이 있는 경우와 두 노드를 잇는 간선이 여럿인 경우가 반례가 되어서 안됨
# A > B > C와 A > C간선이 둘다 있을경우 먼저 탐색된 ABC에 의해 C가 vistied되버려서 AC간선이 더 짧더라도 확인을 하지 못하게됨
# A > B 간선이 10개정도 있을경우 제일 먼저 탐색된 간선의 cost만 체크해서 나머지 간선은 확인못하게됨
import sys
input= sys.stdin.readline

n,m,r = map(int,input().split())

arr = [[sys.maxsize]*n for _ in range(n)]
item = {}
for i,num in enumerate(map(int,input().split())):
    item[i] = num
for _ in range(r):
    a,b,cost = map(int,input().split())
    if cost<arr[a-1][b-1]:
        arr[a-1][b-1] =cost
        arr[b-1][a-1] =cost


for mid in range(n):
    for st in range(n):
        for en in range(n):
            if st==en: arr[st][en] = 0
            if arr[st][en] > arr[st][mid]+arr[mid][en]:
                arr[st][en] = arr[st][mid]+arr[mid][en]
max_farm = 0
for st in range(n):
    farm = 0
    for en in range(n):
        farm += item[en] if arr[st][en] <= m else 0
    max_farm = max(max_farm,farm)
print(max_farm)

###########################################
# import sys
# input= sys.stdin.readline

# n,m,r = map(int,input().split())
# item = [0]*(n+1)
# for i,num in enumerate(map(int,input().split())):
#     item[i+1] = num
# adj = {i:[] for i in range(1,n+1)}
# for _ in range(r):
#     a,b,cost = map(int,input().split())
#     adj[a].append([b,cost])
#     adj[b].append([a,cost])

# def dfs(cur,m):
#     vis[cur] = True
#     farm = item[cur]
#     for dir,cost in adj[cur]:
#         if not vis[dir] and m>=cost:
#             farm += dfs(dir,m-cost)
#     return farm


# max_farm = 0
# for i in range(1,n+1):
#     vis = [False] * (n+1)
#     max_farm = max(max_farm,dfs(i,m))

# print(max_farm)

