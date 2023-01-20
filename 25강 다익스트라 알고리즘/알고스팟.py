# 벽이 아닌곳에서 벽으로 이동하면 비용발생
# (1,1)에서 (n,m) 으로 가는 최소비용
# 노드갯수 n*m = 10^4, 간선 각 노드마다 *4 = 10^4 양의 가중치만 있기에 다익스트라 사용가능


import sys
from heapq import heappop, heappush

inf = float("inf")
input= sys.stdin.readline
m,n = map(int,input().split())
arr = []
nx = [1,0,-1,0]
ny = [0,1,0,-1]
for _ in range(n):
    arr.append(input().rstrip())


def dijkstra():
    q = []
    dis = [[inf]*(m+1) for _ in range(n+1)]
    dis[1][1] = 0
    heappush(q,(0,1,1))

    while q:
        cur_dis,cur_x,cur_y = heappop(q)
        if cur_dis != dis[cur_x][cur_y]: continue

        for i in range(4):
            dx = cur_x + nx[i]
            dy = cur_y + ny[i]

            if 0<dx<=n and 0<dy<=m and dis[dx][dy] > dis[cur_x][cur_y]+int(arr[dx-1][dy-1]):
                dis[dx][dy] = dis[cur_x][cur_y]+int(arr[dx-1][dy-1])
                heappush(q,(dis[dx][dy],dx,dy))
    return dis[n][m]

print(dijkstra())