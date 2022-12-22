import sys
input = sys.stdin.readline
arr = []
n = int(input())

for i in range(n):
    templist = [0]*(n-i-1)
    arr.append(list(map(int,input().split()))+templist)

d= [[0 for _ in range(n)] for _ in range(n)]
d[0][0] = arr[0][0]

for i in range(1,n):
    for j in range(n):
        if j==0:
            d[i][j] = d[i-1][j] + arr[i][j]
        elif j==i:
            d[i][j] = d[i-1][j-1] + arr[i][j]
            break
        else:
            d[i][j] = max(d[i-1][j-1],d[i-1][j])+arr[i][j]
print(max(d[n-1]))

