# 이진탐색트리였으면 걍 [mid] 했으면 될텐데
# 0.1초, N = 10^5, O(N)내지 O(NlogN)해야될듯
# 가운데를 기준으로 가운데보다 작은쪽에서 maxheap, 큰쪽에서 minheap만 꺼내서 비교하면될듯

import sys
from heapq import heappop, heappush

input = sys.stdin.readline
n = int(input())
maxheap = []
minheap = []

heappush(maxheap,-int(input()))
print(-maxheap[0])

for _ in range(1,n):
    x = int(input())
    if x < -maxheap[0]:
        heappush(maxheap,-x)
        if len(maxheap) > len(minheap)+1: heappush(minheap,-heappop(maxheap))

    else:
        heappush(minheap,x)
        if len(minheap) > len(maxheap): heappush(maxheap,-heappop(minheap))
    
    print(-maxheap[0])

