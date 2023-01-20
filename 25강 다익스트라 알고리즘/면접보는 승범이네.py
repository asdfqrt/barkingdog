#노드 갯수 10^5 플로이드 사용불가
# 간선을 거꾸로 입력해서 면접장에서 각 도시로 다익스트라 해서 제일 큰값
# TLE, 다익스트라 > 10^5, 면접장 10^5 라서 10^10인듯
# 다익스트라를 시작할때 큐에 모든 인터뷰지점을 넣고 시작하면 한번으로 됨
# 기본적으로 다익스트라는 한개점에서 다른 모든지점까지의 최소거리지만 이건 큐에 보통 한개 넣고 시작하니까 그런거고
# 여러개 넣으면 그점들을 모두 시작점으로 해서 그 점들에서의 최소거리가 되나봄

import sys
from heapq import heappop, heappush

inf = float("inf")
input= sys.stdin.readline
n,m,k = map(int,input().split())
adj = {i:[] for i in range(1,n+1)}

for _ in range(m):
    a,b,cost = map(int,input().split())
    adj[b].append((a,cost))

interview = set(map(int,input().split()))



q = []
dis = [inf]*(n+1)
for st in interview:
    dis[st] = 0
    heappush(q,(0,st))

while q:
    cur_dis,cur = heappop(q)
    if cur_dis != dis[cur]: continue
    for dir,cost in adj[cur]:
        if dis[dir] > dis[cur]+cost:
            dis[dir] = dis[cur]+cost
            heappush(q,(dis[dir],dir))


max_time = 0
max_town = 0
for i in range(1,n+1):
    if dis[i] > max_time:
        max_time = dis[i]
        max_town = i

print(max_town)
print(max_time)  
















###############################
# import sys
# from heapq import heappop, heappush

# inf = float("inf")
# input= sys.stdin.readline
# n,m,k = map(int,input().split())
# adj = {i:[] for i in range(1,n+1)}

# for _ in range(m):
#     a,b,cost = map(int,input().split())
#     adj[b].append((a,cost))

# interview = set(map(int,input().split()))


# def dijkstra(start):
#     q = []
#     dis = [inf]*(n+1)
#     dis[start] = 0
#     heappush(q,(0,start))

#     while q:
#         cur_dis,cur = heappop(q)
#         if cur_dis != dis[cur]: continue
#         for dir,cost in adj[cur]:
#             if dis[dir] > dis[cur]+cost and dir not in interview:   #이거 제거안해주면 TLE
#                 dis[dir] = dis[cur]+cost
#                 heappush(q,(dis[dir],dir))
#     return dis[1:]

# min_time = [inf]*n

# for i in interview:
#     for j,time in enumerate(dijkstra(i)):
#         min_time[j] = min(min_time[j],time)


# max_town = 0
# max_time = 0
# for town,time in enumerate(min_time):
#     if time > max_time:
#         max_time = time
#         max_town = town+1

# print(max_town)
# print(max_time)