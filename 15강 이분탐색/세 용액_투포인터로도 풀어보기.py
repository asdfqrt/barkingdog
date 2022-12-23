import bisect
import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
ans1 = 1e9+1
ans2 = 1e9+1
ans3 = 1e9+1


for i in range(n-1):
    for j in range(i+1,n):
        two = arr[i]+arr[j]
        idx = bisect.bisect_left(arr,-two,lo=j+1)

        if idx+1 < n and abs(two+arr[idx+1]) < abs(ans1+ans2+ans3):  #two+arr[idx]와 더했을때 가장 작은 원소는 a[idx+1] or a[idx] or a[idx-1]
            ans1 = arr[i]
            ans2 = arr[j]
            ans3 = arr[idx+1]
        if idx < n and abs(two+arr[idx]) < abs(ans1+ans2+ans3):
            ans1 = arr[i]
            ans2 = arr[j]
            ans3 = arr[idx]
        if idx-1 > j and abs(two+arr[idx-1]) < abs(ans1+ans2+ans3):
            ans1 = arr[i]
            ans2 = arr[j]
            ans3 = arr[idx-1]

print(*sorted([ans1,ans2,ans3]))



#나중에 투포인터로 다시 풀어봐야될듯