# N = 10^5 제한시간 1초 O(N^2) 하면 10초걸리겟는데

import sys
input = sys.stdin.readline

n,k = map(int,input().split())
arr = list(map(int,input().split()))
isused = [0]*100001
isused[arr[0]] = 1

en = 0
ans = 0

for st in range(n):
    while en<n-1 and isused[arr[en+1]] < k:
        en += 1
        isused[arr[en]] += 1
    ans = max(en-st+1,ans)
    if en==n-1: break
    isused[arr[st]] -= 1
print(ans)