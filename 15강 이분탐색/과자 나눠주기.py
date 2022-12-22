m,n = map(int,input().split())
arr = list(map(int,input().split()))
done = False

def solve(x):   #막대과자의 길이가 x일 때 m명의 조카에게 나눠줄 수 있는가
    cur = 0
    for i in arr:
        cur += i//x
    return cur >= m


st = 1
ed = max(arr)

while st<ed:
    mid = (st+ed+1)//2
    if solve(mid):
        st = mid
        done = True
    else:
        ed = mid-1
print(st if done else 0)