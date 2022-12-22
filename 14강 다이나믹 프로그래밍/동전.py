# import sys
# input = sys.stdin.readline

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     coin = list(map(int,input().split()))
#     m = int(input())
#     d=[1]+[0 for _ in range(10000)]

#     for i in range(n):
#         for j in range(coin[i],m+1):
#             d[j] += d[j-coin[i]]
#     print(d[m])


import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    coin = list(map(int,input().split()))
    m = int(input())
    d=[1]+[0 for _ in range(10000)]

    for i in coin:
        for j in range(i,m+1):
            d[j] += d[j-i]
    print(d[m])