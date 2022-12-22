# import sys
# input = sys.stdin.readline

# n = int(input())
# x = list(map(int,input().split()))
# inv_sum = 0
# tmax = x[0]

# for l in range(n):
#     for r in range(l,n):
#         inv_sum += x[r]
#         tmax = max(tmax,inv_sum)
#     inv_sum = 0
# print(tmax)

# import sys
# input = sys.stdin.readline
# n=int(input())
# x = list(map(int,input().split()))
# sum = 0
# d =[]
# tmax = x[0]
# for i in x:
#     sum += i
#     d.append(sum)

# for i in range(1,len(d)):
#     tmax = max(tmax,d[i]-min(d[:i]))

# print(tmax)

import sys
input = sys.stdin.readline
n=int(input())
x = list(map(int,input().split()))
d=[x[0]]

for i in range(1,n):
    d.append(x[i])
    d[i] = max(d[i],d[i-1]+x[i])
print(max(d))
