################################
#이분탐색

# import sys
# import bisect
# input = sys.stdin.readline

# n,m = map(int,input().split())
# arr = []
# for _ in range(n):
#     arr.append(int(input()))
# arr.sort()

# minsub = 1e10+1
# for i in range(n):
#     idx =  bisect.bisect_left(arr,arr[i]+m)
#     if idx != n:
#         minsub = min(minsub,arr[idx]-arr[i])
# print(minsub)



###############################
#투 포인터
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

st = 0
en = 0
minsub = sys.maxsize    #시스템 최대값
while st<n-1 and en<n:
    if arr[en]- arr[st] >= m:
        minsub=min(minsub,arr[en]-arr[st])
        st += 1
    else:
        en += 1
print(minsub)