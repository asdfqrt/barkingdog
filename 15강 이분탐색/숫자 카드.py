

# input()
# have = list(map(int,input().split()))
# have.sort()
# input()
# check = list(map(int,input().split()))

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

# for i in check:
#     print(1 if binary(i,have) else 0, end =" ")


##########################################
input()
have = set(input().split()) #set으로 해야 in에서 시간초과 안남
input()
check = input().split()

for i in check:
    print(1 if i in have else 0, end = " ")