# import sys
# import bisect

# input = sys.stdin.readline
# n = int(input())
# arr = list(map(int,input().split()))
# ans1 = arr[0]
# ans2 = arr[1]

# for i in arr:
#     idx = bisect.bisect_left(arr,-i)


#     if idx == n:
#         idx = idx-1
    
#     if idx !=0 and abs(arr[idx]+i) > abs(arr[idx-1]+i):
#         idx = idx-1
    
#     if arr[idx] != i and abs(ans1+ans2) > arr[idx]+i:
#         ans1 = i
#         ans2 = arr[idx]
    
# print(*sorted([ans1,ans2]))



import bisect
import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
ans1 = 1e9+1
ans2 = 1e9+1

for i in range(n):
    idx = bisect.bisect_left(arr,-arr[i])

    if idx+1 < n and i!=idx+1 and abs(arr[i]+arr[idx+1]) < abs(ans1+ans2):  #a[i]와 더했을때 가장 작은 원소는 a[idx+1] or a[idx] or a[idx-1]
        ans1 = arr[i]
        ans2 = arr[idx+1]
    if idx < n and i!=idx and abs(arr[i]+arr[idx]) < abs(ans1+ans2):
        ans1 = arr[i]
        ans2 = arr[idx]
    if idx-1 >= 0 and i!=idx-1 and abs(arr[i]+arr[idx-1]) < abs(ans1+ans2):
        ans1 = arr[i]
        ans2 = arr[idx-1]

print(*sorted([ans1,ans2]))