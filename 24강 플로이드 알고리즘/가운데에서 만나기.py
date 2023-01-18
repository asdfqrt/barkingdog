#플로이드로 모든거리 다 구한다음에 for 돌려서 왕복 시간이 제일 짧은 곳 찾아

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [[sys.maxsize]*n for _ in range(n)]
for _ in range(m):
    a,b,cost = map(int,input().split())
    if arr[a-1][b-1] > cost:
        arr[a-1][b-1] = cost

k = int(input())
livetown = list(map(int,input().split()))


for mid in range(n):
    for st in range(n):
        for en in range(n):
            if st==en: arr[st][en]=0
            if arr[st][en] > arr[st][mid] + arr[mid][en]:
                arr[st][en] = arr[st][mid] + arr[mid][en]

min_dis = sys.maxsize
townlist = []
for point in range(n):
    point_dis = 0
    for friend in livetown:
        point_dis = max(point_dis,arr[friend-1][point] + arr[point][friend-1])
    if point_dis == min_dis:
        townlist.append(point+1)
    elif point_dis < min_dis:
        townlist = [point+1]
        min_dis = point_dis

print(*townlist)

    
