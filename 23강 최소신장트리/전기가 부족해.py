# 크루스칼 알고리즘으로 하면안될듯? > 비용이 작은 간선이 도시를 두 발전소와 연결시켜버릴수있음
# 프림 알고리즘으로 시작가능지점인 발전소 인접 간선들을 heapq에 넣은후, heappop으로 간선과 연결된 노드에 인접한 간선들 다시 heapq에 넣으면 될거같음
# 발전소에서는 나가는 방향만, 들어오는거는 하면xxx
# 필요한 간선의 갯수 = (노드 갯수-1) - (발전소 갯수-1) = 노드갯수 - 발전소갯수
import sys
from heapq import heappop, heappush

input=sys.stdin.readline

n,m,k = map(int,input().split())
vis = set(map(int,input().split()))
adj = {i:[] for i in range(1,n+1)}
heap = []
for _ in range(m):
    a,b,cost = map(int,input().split())
    adj[a].append([b,cost])
    adj[b].append([a,cost])

    if a in vis:
        heappush(heap,[cost,a,b])
    if b in vis:
        heappush(heap,[cost,b,a])
power = len(vis)
ans = 0
cnt = 0
while cnt<n-power:
    cost,a,b = heappop(heap)
    if b in vis: continue
    ans += cost
    vis.add(b)
    cnt +=1
    for dir,cost in adj[b]:
        if dir not in vis:
            heappush(heap,[cost,b,dir])
print(ans)

###############
#크루스칼 알고리즘으로 풀수있음
#가상의 노드 0과 발전기들을 간선으로 이어버리면 됨 > 발전기들이 같은 그룹에 들어와버리니 자연스럽게 이후 간선에서 연결될일 x
#이후에는 MST찾기