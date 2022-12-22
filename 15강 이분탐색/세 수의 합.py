# from itertools import combinations_with_replacement
# import sys
# input = sys.stdin.readline
# n = int(input())
# u = []
# two = []

# for _ in range(n):
#     u.append(int(input()))

# for i in combinations_with_replacement(u,2):
#     two.append(sum(i))

# u.sort(reverse=True)
# two.sort()


# def binary(target,arr):
#     st = 0
#     ed = len(arr)-1
#     while st<=ed:
#         mid = (st + ed) //2
#         if target == arr[mid]:
#             return True
#         elif target > arr[mid]:
#             st = mid +1
#         elif target < arr[mid]:
#             ed = mid -1
#     return False



# for i in u:
#     for j in u:
#         if binary(i-j,two):
#             print(i)
#             exit()

##################################################
# n = int(input())
# u = sorted([int(input()) for _ in range(n)])
# add_two = set()

# for i in u:
#     for j in u:
#         add_two.add(i+j)

# for i in u[::-1]:
#     for j in u[::-1]:
#         if i-j in add_two:
#             print(i)
#             exit()
##################################################

from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline
n = int(input())
u = []
two = set()  #두수의 합 two를 set() 집합자료형으로 두고 시작해야 i-j in two를 검색할때 시간초과가 안남. 리스트로 하면 in 검색시 오래걸려 binary 함수 따로 써야됨

for _ in range(n):
    u.append(int(input()))

for i in combinations_with_replacement(u,2):
    two.add(sum(i))
u.sort(reverse=True)

for i in u:
    for j in u:
        if i-j in two:
            print(i)
            exit()