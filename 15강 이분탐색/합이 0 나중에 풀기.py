import bisect
import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
cnt = 0

for i in range(n-1):
    for j in range(i+1,n):
        st = bisect.bisect_left(arr,-arr[i]-arr[j],lo=j+1)  #lo hi로 범위설정가능
        ed = bisect.bisect_right(arr,-arr[i]-arr[j],lo=j+1)
        cnt += ed-st
print(cnt)



#이분탐색으로는 시간 부족해서 안풀린듯




