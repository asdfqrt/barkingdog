# import sys
# input = sys.stdin.readline

# input()
# x = list(map(int,input().split()))
# x_s = sorted(set(x))

# def idx(target):
#     st = 0
#     ed = len(x_s)
#     while st<ed:
#         mid = (st+ed)//2
#         if x_s[mid] >=target:
#             ed = mid
#         else:
#             st = mid+1
#     return st

# for target in x:
#     print(idx(target), end =" ")

##################################################
CN=int(input())
A=list(map(int,input().split()))
B=list(set(A))
B.sort()
C={}
for i in range(len(B)): C[B[i]]=i
for w in A: print(C[w],end=' ')
###################################################
