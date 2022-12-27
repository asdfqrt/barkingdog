# 제한시간 1초 테스트케이스 10^2개, 해빈이가 가진 의상수 30개  (headgear+1() * (eyewear+1) ... -1 하면될듯

import sys
input =sys.stdin.readline


for _ in range(int(input())):
    arr = {}
    gearnum = int(input())
    cnt = 1

    for _ in range(gearnum):
        _, gear = input().split()
        if gear in arr:
            arr[gear] += 1
        else:
            arr[gear] = 1

    for i in arr.values():  #arr.values()가 arr.items()쓰고 [1] 찾는거 그대로 나옴
        cnt *= (i+1)
    print(cnt-1)

    # for i in arr.items():
    #     cnt = cnt * (i[1]+1)
    # print(cnt-1)

