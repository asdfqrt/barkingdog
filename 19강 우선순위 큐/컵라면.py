#그냥 제일 데드라인이 빠른거 부터 하나씩 처리하는방식은 안좋을듯?
#ex)데드라인 1에 3개 컵라면, 2에 10개 컵라면,2에 9개 컵라면이면 데드라인1버리는게 나음
# 2초, 숙제의 갯수 10^5 데드라인 10^5, 컵라면 1~n까지돌면서 push pop 하면 O(nlogn) >> 충분할듯

import sys
from heapq import heappop, heappush, heappushpop
input= sys.stdin.readline

n = int(input())
arr = []
ans = []
for i in range(n):
    dl,cn = map(int,input().split())
    heappush(arr,[dl,-cn])

for i in range(n):
    try:
        heappush(ans, -heappop(arr)[1])
        while arr[0][0]<=i+1:
            temp = heappop(arr)
            if -temp[1] > ans[0]: heappushpop(ans, -temp[1])
    except:
        print(sum(ans))
        exit()

######################################
import sys
import heapq

input = sys.stdin.readline

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort()

queue = []

for deadline, reward in arr:
    heapq.heappush(queue, reward)
    if deadline < len(queue):
        heapq.heappop(queue)

print(sum(queue))
###################################