n,m = map(int,input().split())
arr = list(map(int,input().split()))

def check(x):   #절단기의 높이가 m의 나무길이를 구할수 있는가
    cur = 0
    for i in arr:
        rest = i-x
        if rest >0:
            cur += rest
    return cur >= m

st = 0
ed = max(arr)

while st<ed:
    mid = (st+ed+1)//2
    if check(mid):
        st=mid
    else:
        ed=mid-1
print(st)