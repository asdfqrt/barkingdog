# arr[st][en] + arr[en][st]의 최소값
# 노드 400개정도, 플로이드 와샬로 싹다 구하면될듯
# TLE뜸 상수시간줄이기?

import sys

input= sys.stdin.readline
v,e = map(int,input().split())
arr = [[sys.maxsize]*v for _ in range(v)]
for _ in range(e):
    #쌍이 같은 도로 여러번 안주어지니 대소관계 비교 필요 x
    a,b,cost =map(int,input().split())
    arr[a-1][b-1] = cost

for mid in range(v):
    for st in range(v):
        for en in range(v):
            if arr[st][en] > arr[st][mid] + arr[mid][en]:
                arr[st][en] = arr[st][mid] + arr[mid][en]
min_dis = sys.maxsize
for st in range(v):
    for en in range(v):
        dis = arr[st][en]+arr[en][st]
        if min_dis>dis: min_dis = dis
print(min_dis if min_dis!=sys.maxsize else -1)
