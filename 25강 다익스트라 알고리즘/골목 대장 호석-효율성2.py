# 노드 10^5, 간선 10^5, 사이클 O, 음수간선x
# 시작에서 도착까지 최저비용 > 다익스트라
# 수치심을 줄이고 싶을 수록 같거나 더 많은 돈이 필요하고 수치심을 더 받는 것을 감수하면 같거나 더 적은 돈이 필요하게 된다는 것을 알게 되었다
# 이 말이 parametric search의 힌트
# 다익스트라에서 x 수치심 제한으로 목표노드 도달 가능한지 여부반환하고 이를 parametric search한다

import sys
from heapq import heappush, heappop

input = sys.stdin.readline
inf = float("inf")
n,m,start,end,money = map(int,input().split())
adj = {i:[] for i in range(1,n+1)}
for _ in range(m):
    a,b,cost = map(int,input().split())
    adj[a].append((b,cost))
    adj[b].append((a,cost))



def dijkstra(limit):
    dis = [inf]*(n+1)
    dis[start] = 0
    q = []
    heappush(q,(0,start))

    while q:
        cur_dis,cur = heappop(q)
        if dis[cur] != cur_dis: continue
        for dir,cost in adj[cur]:
            if cost > limit: continue
            nxt_cost = dis[cur]+cost
            if nxt_cost > money: continue
            if dis[dir] > nxt_cost:
                if dir==end:
                    return True
                dis[dir] = nxt_cost
                heappush(q,(dis[dir],dir))

    return False
#parametric search
st=0
en=money
while st<en:
    mid = (st+en)//2
    if dijkstra(mid):
        en = mid
    else:
        st = mid+1
print(st if dijkstra(st) else -1)