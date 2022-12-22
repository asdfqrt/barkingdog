n=int(input())
d=[0,1,1]
for i in range(3,n+1):
    d.append(d[i-2]+ d[i-1])
print(d[n])


# n = int(input())
# a,b = 1,1
# for i in range(1,n):
#     a,b = b,a+b
# print(a)