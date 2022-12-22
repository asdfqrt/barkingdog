# import sys
# input = sys.stdin.readline

# n = int(input())
# a = list(map(int,input().split()))
# a.sort()
# m = int(input())
# b = list(map(int,input().split()))


# def upper_idx(target,len):
#     st = 0
#     en = len
#     while st<en:
#         mid = (st+en)//2
#         if a[mid] >target:
#             en = mid
#         else:
#             st = mid+1
#     return st


# def lower_idx(target,len):
#     st = 0
#     en = len
#     while st<en:
#         mid = (st+en)//2
#         if a[mid] >=target:
#             en = mid
#         else:
#             st = mid+1
#     return st

# for i in b:
#     print(upper_idx(i,n)-lower_idx(i,n), end=" ")



################################################## 이분탐색 아닌 Counter로 갯수 새주는 새로운 함수
# from collections import Counter
# import sys

# input = sys.stdin.readline
# input()
# counter = Counter(input().split())
# input()
# for i in input().split():
#     print(counter[i],end=" ")
################################################## bisect 이분탐색 내장함수 걍 이거만 쓰면 될듯

import sys
import bisect

input = sys.stdin.readline

input()
a = list(map(int,input().split()))
a.sort()
input()
b = list(map(int,input().split()))


for i in b:
    print(bisect.bisect_right(a,i)-bisect.bisect_left(a,i), end=" ")