import sys
from collections import deque
input= sys.stdin.readline

n=int(input())
arr = list(map(int,input().split()))
st=0
en=0
ans=0
cur = set()
cur.add(arr[0])
for st in range(n):
    while en < n-1 and arr[en+1] not in cur:
        en+=1
        cur.add(arr[en])
    ans += en-st+1  #수열의 길이가 곧 그st로 시작하는 수열에서 나오는 부분수열들의 경우의 수 ex) (1,2,3,4,5)는 (1), (1,2), (1,2,3), (1,2,3,4), (1,2,3,4,5)를 1로시작하는 부분수열로 가진다
    cur.remove(arr[st])

print(ans)


