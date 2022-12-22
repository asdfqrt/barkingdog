# import sys
# input = sys.stdin.readline


# n = int(input())
# a = list(map(int,input().split()))
# a.sort()

# m = int(input())
# mlist = list(map(int,input().split()))

# for i in mlist:
#     st = 0
#     ed = n-1
#     while True:
#         mid = (st + ed) //2
#         if i == a[mid]:
#             print(1)
#             break
#         elif ed < st:
#             print(0)
#             break
#         elif i > a[mid]:
#             st = mid +1
#         elif i < a[mid]:
#             ed = mid -1

import sys
input = sys.stdin.readline

input()
alist = set(input().split())
input()
for i in input().split():
    print(int(i in alist))