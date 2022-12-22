# data = list(range(1,21))
# for i in range(10):
#     where = list(map(int,input().split()))
#     if where[0] == where[1]:
#         continue
#     bande = data[where[0]-1:where[1]]
#     bande.reverse()
#     del data[where[0]-1:where[1]]
    
#     t = 0
#     for j in range(where[0]-1,where[1]):
#         data.insert(j,bande[t])
#         t = t + 1
# print(*data)


A = list(range(1,21))
for _ in range(10):
    a,b = map(lambda x:int(x)-1,input().split())
    A[a:b+1] = A[a:b+1][::-1]
print(*A)