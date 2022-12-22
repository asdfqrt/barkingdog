import bisect

arr = []
k,n = map(int,input().split())
for _ in range(k):
    arr.append(int(input()))



def solve(x):   #랜선의 길이가 X일때 랜선이 N개 이상인가 아닌가
    cur = 0
    for i in arr:
        cur += i//x
    return cur >= n

st = 1
en = max(arr)

while st<en:    #랜선의 길이를 이분탐색으로 찾기 << 랜선길이에 따라 갯수가 정렬되어있기에 가능
    mid = (st+en+1)//2  #st+en 하면 무한 루프에 빠짐
    if solve(mid):
        st=mid
    else:
        en=mid-1
print(st)