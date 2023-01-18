# 일방통행 정방향은 비용 0, 역방향은 비용 1
# 양방향은 둘다 비용 0
# arr[st][en]의 비용이 양방향으로 바꿔야되는 갯수임

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [[sys.maxsize]*n for _ in range(n)]
for _ in range(m):
    a,b,cost = map(int,input().split())
    arr[a-1][b-1] = 0
    arr[b-1][a-1] = 0 if cost==1 else 1

for mid in range(n):
    for st in range(n):
        for en in range(n):
            if st==en: arr[st][en]=0
            if arr[st][en] > arr[st][mid] + arr[mid][en]:
                arr[st][en] = arr[st][mid] + arr[mid][en]

k=int(input())
for _ in range(k):
    a,b = map(int,input().split())
    print(arr[a-1][b-1])