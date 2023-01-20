# 다익스트라는 한 노드에서 다른노드로 가는 최소 거리, 양방향이 아니니 어짜피 모든 노드에 대해 다익스트라 시행해야되는거인듯?
# 그럴꺼면 플로이드 와샬과 다를거 없지 않나?>> 플로이드
# TLE남, 노드 1000개, 간선 10000개인데도 안되네 >> 다익스트라

# v가 노드갯수, e가 간선갯수일때 플로이드 와샬은 O(V^3), 다익스트라는 O(ElogE)
# 본 문제에서 플로이드 와샬 하면 (10^3)^3 = 10^9로 1초 빠듯이지만 다익스트라는 O(V * ElogE) = 10^3 * 10^4 * 4 = 10^7으로 더 빠름
# 걍 이후로 간선이 음수인 경우만 플로이드, 그거빼곤 전부 다익스트라로 쓰는게 더 빠름
# 단지 간선의 크기 E가 V^3 보다 커지는 경우  ElogE > V^3 * 3 logV > V^3 으로 플로이드가 빠를수있음(거의 안나옴 노드 10^3이면 간선 10^9개이상일때)

# 이 문제는 도착지점이 x로 정해져 있으므로 다익스트라를 딱 두번만 돌려서 알수있다(각자 집에서 x가 아닌곳으로 가는 비용 계산이 필요없기 때문)
# 돌아오는길은 x에서 출발하여 모든 노드로 뻗어나가니 일반적인 다익스트라
# 모든 정점에서 x로 가는 최단거리를 구하려면 간선의 방향을 전부 뒤집은 다음 x에서 시작하는 다익스트라 알고리즘을 돌림
# "x에서 y로 가는 경로"의 간선의 방향을 뒤집으면 "y에서 x로 가는 경로"가 되기 때문
# O(N) = 10^4 *4 + 10^4 *4 ~= 10^4

import sys
from heapq import heappop, heappush

inf = float("inf")
input= sys.stdin.readline
n,m,x = map(int,input().split())
adj1 = {i:[] for i in range(1,n+1)}
adj2 = {i:[] for i in range(1,n+1)}
for _ in range(m):
    a,b,cost = map(int,input().split())
    adj1[a].append((b,cost))
    adj2[b].append((a,cost))


def dijkstra(start,adj):
    q = []
    dis = [inf]*(n+1)
    dis[start] = 0
    heappush(q,(0,start))

    while q:
        cur_dis,cur = heappop(q)
        if cur_dis != dis[cur]: continue
        for dir,cost in adj[cur]:
            if dis[dir] > dis[cur]+cost:
                dis[dir] = dis[cur]+cost
                heappush(q,(dis[dir],dir))
    return dis[1:]


dis1 = dijkstra(x,adj1) # x를 시작점으로 나머지 집에 가는거(돌아가는길)
dis2 = dijkstra(x,adj2) # 입력을 거꾸로 받았기 때문에 각 마을에서 x오는 최소비용이 나옴
max_time = 0
for i in range(n):
    max_time = max(max_time,dis1[i]+dis2[i])
print(max_time)


#######################################
# import sys
# from heapq import heappop, heappush

# inf = float("inf")
# input= sys.stdin.readline
# n,m,x = map(int,input().split())
# adj = {i:[] for i in range(1,n+1)}

# for _ in range(m):
#     a,b,cost = map(int,input().split())
#     adj[a].append((b,cost))


# dis = [[inf]*(n+1) for _ in range(n+1)]

# for friend in range(1,n+1):
#     q = []
#     dis[friend][friend] = 0
#     heappush(q,(0,friend))

#     while q:
#         cur_dis,cur = heappop(q)
#         if cur_dis != dis[friend][cur]: continue
#         for dir,cost in adj[cur]:
#             if dis[friend][dir] > dis[friend][cur]+cost:
#                 dis[friend][dir] = dis[friend][cur]+cost
#                 heappush(q,(dis[friend][dir],dir))



# max_time = 0
# for friend in range(1,n+1):
#     time = dis[friend][x] + dis[x][friend]
#     max_time = max(max_time,time)
# print(max_time)









# import sys

# input= sys.stdin.readline
# n,m,x = map(int,input().split())

# arr = [[float("inf")]*n for _ in range(n)]
# for _ in range(m):
#     a,b,cost = map(int,input().split())
#     arr[a-1][b-1] = cost
# for mid in range(n):
#     for st in range(n):
#         for en in range(n):
#             if st==en: arr[st][en] = 0
#             if arr[st][en] > arr[st][mid] + arr[mid][en]:
#                 arr[st][en] = arr[st][mid] + arr[mid][en]
# max_dis = 0
# for friend in range(n):
#     dis = arr[friend][x-1] + arr[x-1][friend]
#     max_dis = max(max_dis,dis)
# print(max_dis)

