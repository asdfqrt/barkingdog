#플로이드 와샬 하면서 nxt배열 구하는거


import sys
input= sys.stdin.readline

n,m = map(int,input().split())

arr = [[sys.maxsize]*n for _ in range(n)]
nxt = [[-1]*n for _ in range(n)]
for _ in range(m):
    a,b,cost = map(int,input().split())
    if arr[a-1][b-1] > cost:    #두 노드있는 간선 두개이상 주어질경우 짧은것만 탄다
        arr[a-1][b-1] = cost
        arr[b-1][a-1] = cost
        nxt[a-1][b-1] = b-1
        nxt[b-1][a-1] = a-1

for mid in range(n):
    for st in range(n):
        for en in range(n):
            if st==en: arr[st][en] =0
            if arr[st][en] > arr[st][mid] + arr[mid][en]:
                arr[st][en] = arr[st][mid] + arr[mid][en]
                nxt[st][en] = nxt[st][mid]
for i in nxt:
    for j in i:
        print(j+1 if j!=-1 else "-",end=" ")
    print()