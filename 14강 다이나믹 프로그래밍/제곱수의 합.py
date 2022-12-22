# isused = [0 for _ in range(316)]
# n = int(input())


# for i in range(316,0,-1):
#     while n-i**2>=0:
#         isused[i-1]+=1
#         n -= i**2
# print(sum(isused))


n = int(input())
d=[0,1,2,3,1]

for i in range(5,n+1):
    root = int(i**(1/2))
    d.append(d[i-1]+1)
    for j in range(2,root+1):
        d[i] = min(d[i],d[i-j*j]+1)
print(d[n])
    