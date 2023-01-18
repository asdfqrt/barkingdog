
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [[sys.maxsize]*n for _ in range(n)]
nxt = [[0]*n for i in range(n)]
for _ in range(m):
    a,b,cost = map(int,input().split())
    if cost<arr[a-1][b-1]:
        arr[a-1][b-1] =cost
        nxt[a-1][b-1] = b-1

for mid in range(n):
    for st in range(n):
        for en in range(n):
            if st==en: arr[st][en] = 0
            if arr[st][en] > arr[st][mid]+arr[mid][en]:
                arr[st][en] = arr[st][mid]+arr[mid][en]
                nxt[st][en] = nxt[st][mid]

for st in range(n):
    for en in range(n):
        print(arr[st][en] if arr[st][en]!= sys.maxsize else 0,end=" ")
    print()

for st in range(n):
    for en in range(n):
        if arr[st][en] == sys.maxsize or arr[st][en] == 0:
            print(0)
            continue
        
        cur = st
        path = []
        while cur != en:
            path.append(cur+1)
            cur = nxt[cur][en]
        path.append(en+1)
        print(len(path),*path)

