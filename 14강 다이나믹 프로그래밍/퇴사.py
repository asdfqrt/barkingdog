import sys
input = sys.stdin.readline
n = int(input())
d = [0 for _ in range(n)]


for i in range(n):
    t,p = map(int,input().split())


    if i==0:
        try:
            d[t-1]=p
            continue
        except:
            continue
    d[i] = max(d[i],d[i-1])
    try:
        d[i+t-1] = max(d[i+t-1],d[i-1]+p)
    except:
        continue

print(d[n-1])