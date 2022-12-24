import sys
import bisect

input = sys.stdin.readline
n,c = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

def check(x):   #x길이에서 c개 이상의 공유기가 들어갈수 있나
    idx = 0
    cnt = 0
    while idx != n:
        idx = bisect.bisect_left(arr,arr[idx]+x,lo=idx)
        cnt += 1
    return cnt >= c

st = 1
ed = arr[-1]-arr[0]

while st<ed:
    mid = (st+ed+1)//2
    if check(mid):
        st = mid
    else:
        ed = mid-1
print(st)

