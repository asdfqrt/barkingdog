# #시간 제한 1초 N=1500, 힙큐 푸시가 logn이니까 다 넣으면 nlogn+ pop하는데 nlogn이니까 1500연산내외 시간충분

# import sys
# from heapq import heappop, heappush

# input= sys.stdin.readline
# n = int(input())
# arr = []
# for _ in range(n):
#     for i in input().split():
#         heappush(arr,-int(i))
# for _ in range(n-1):
#     heappop(arr)

# print(-arr[0])

#메모리 초과가 나는걸
#n개까지는 그냥 받고 n개 넘어가면 그때부터 heappop으로 작은숫자들 다쳐내
#그럼 pop은 n^2-n번 하게될거고  이후로 pop한번만 더하면 그게 n번째 큰수

import sys
from heapq import heappop, heappush

input= sys.stdin.readline
n = int(input())
arr = []

for i in input().split():
    heappush(arr,int(i))

for _ in range(1,n):
    for i in input().split():
        heappush(arr,int(i))    #먼저 받고나서 pop해야 마지막까지 비교됨
        heappop(arr)

print(arr[0])