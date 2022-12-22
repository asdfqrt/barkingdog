n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
arr = [[0,0,0]]+ arr
c = [[0,0,0],[arr[1][0],arr[1][1],arr[1][2]]]

for i in range(2,n+1):
    c.append([min(c[i-1][1],c[i-1][2])+arr[i][0],
    min(c[i-1][0],c[i-1][2])+arr[i][1],
    min(c[i-1][0],c[i-1][1])+arr[i][2]])

print(min(c[n]))
