# n = int(input())

# toone = [0,0,1,1]+[0 for _ in range(n)]
# cnt = []
# for i in range(4,n+1):
#     if i%3==0:
#         toone[i]=toone[i//3]+1
#         cnt.append(i//3)
#     elif i%2==0:
#         toone[i]=toone[i//2]+1
#         cnt.append(i//2)
#     else:
#         toone[i]=toone[i-1]+1
#         cnt.append(i-1)

# print(toone[n])
# print(*cnt)

n = int(input())
d = [0,0]
pre = [0,0]

for i in range(2,n+1):
    d.append(d[i-1]+1)
    pre.append(i-1)
    if i%2==0 and d[i]>d[i//2]+1:
        d[i] = d[i//2]+1
        pre[i] = i//2
    if i%3==0 and d[i]>d[i//3]+1:
        d[i] = d[i//3]+1
        pre[i] = i//3
print(d[n])
cur = n
while True:
    print(cur)
    if cur==1: break
    cur = pre[cur]