#허프만코딩 찾아보기 매번 가장 작은 두개의 원소 빼서 더하기

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())
arr = []
ans = 0
for _ in range(n): heappush(arr,int(input()))
for _ in range(n-1): #비교할때마다 한개씩 줄어드니까
    temp =  heappop(arr)+heappop(arr)
    ans += temp
    heappush(arr,temp)
print(ans)
