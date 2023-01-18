# 문제의 표현이 구림, 도시사이의 최소이동시간이 틀렸으면 -1 출력


import sys

input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

exist = [[True]*n for _ in range(n)]
for mid in range(n):
    for st in range(n):
        for en in range(n):
            if arr[st][en] > arr[st][mid] + arr[mid][en]:
                print(-1)
                exit()
            if st!=mid and en!=mid and st!=en and arr[st][en] == arr[st][mid] + arr[mid][en]: #mid 들럿다와도 같은 시간이면 굳이 이 직통도로가 있을 필요가 없음
                exist[st][en] = False
ans = 0
for st in range(n):
    for en in range(n):
        if exist[st][en]:
            ans += arr[st][en]
print(ans//2)   #왕복 두번 더해짐
