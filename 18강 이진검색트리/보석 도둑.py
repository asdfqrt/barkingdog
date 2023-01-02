# 제일 비싼 보석을 제일 작은 가방에서부터 넣는게 이득


# import sys, heapq
# import bisect
# from collections import defaultdict

# input = sys.stdin.readline
# n,k = map(int,input().split())

# gemlist = []
# for _ in range(n):
#     m,v = map(int,input().split())
#     heapq.heappush(gemlist,[-v,m])

# baglist = []
# bagused = defaultdict(int)
# for _ in range(k):
#     bagsize = int(input())
#     baglist.append(bagsize)
#     bagused[bagsize] +=1

# baglist.sort()

# price = 0

# while gemlist:
#     gem = heapq.heappop(gemlist)
#     idx = bisect.bisect_left(baglist,gem[1])
#     while idx < len(baglist):
#         if bagused[baglist[idx]]>0:
#             price += -gem[0]
#             bagused[baglist[idx]] -= 1
#         else: idx += 1
# print(price)

import sys
from heapq import heappop, heappush

input = sys.stdin.readline
n,k = map(int,input().split())

gemlist = []
for _ in range(n):
    m,v = map(int,input().split())
    heappush(gemlist,[m,v])

baglist = []
for _ in range(k):
    baglist.append(int(input()))
baglist.sort()

price = 0
temp_gem = []

for i in baglist:   #가장 작은 가방부터 시작
    while gemlist and i >= gemlist[0][0]:   #현재 가방의 크기보다 가벼운 보석들이 있다면
        heappush(temp_gem,-heappop(gemlist)[1]) # 보석들을 옮길수 있는 보석으로 분류
    if temp_gem:
        price += -heappop(temp_gem)   #옮길수 있는 보석 중 제일 비싼 보석을 옮김

print(price)