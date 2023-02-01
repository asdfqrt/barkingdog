import sys
input =sys.stdin.readline
n,m = map(int,input().split())
arr = [[0]*(n+1)]
for _ in range(n):
    arr.append([0]+list(map(int,input().split())))

for x in range(1,n+1):
    for y in range(1,n+1):
        arr[x][y] += arr[x-1][y] + arr[x][y-1] - arr[x-1][y-1]
for _ in  range(m):
    x1,y1,x2,y2 = map(int,input().split())
    print(arr[x2][y2]-arr[x1-1][y2]-arr[x2][y1-1]+arr[x1-1][y1-1])
