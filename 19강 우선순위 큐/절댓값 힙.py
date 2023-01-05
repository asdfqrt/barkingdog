#양의 숫자 음의숫자 따로 받은다음 둘다 +만 나오게해서 [0]값 비교하면 제일 절대값이 작은 값끼리 비교가능
from heapq import heappop, heappush
import sys
input = sys.stdin.readline
pheap = []
mheap = []

n = int(input())
for _ in range(n):
    x = int(input())
    if x > 0: heappush(pheap,x)
    elif x < 0: heappush(mheap,-x)
    else:
        if not pheap and not mheap: print(0)
        elif not pheap: print(-heappop(mheap))
        elif not mheap: print(heappop(pheap))
        elif abs(pheap[0]) < abs(mheap[0]): print(heappop(pheap))
        else: print(-heappop(mheap))
####################################################
#그냥 처음부터 하나의 힙에 abs,일반 둘다 받으면 abs를 먼저, 이후에 일반값을 비교하게되어있음

from heapq import heappop, heappush
import sys
input = sys.stdin.readline
heap = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x: heappush(heap,[abs(x),x])
    else: print(heappop(heap)[1] if heap else 0)
