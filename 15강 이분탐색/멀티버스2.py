
m,n = map(int,input().split())
arr = []
arr_s = []
for _ in range(m):
    x = list(map(int,input().split()))
    arr.append(x)
    arr_s.append(sorted(x))

C = {}
for i in range(n):
    C[arr_s[1][i]] = i
for w in arr[1]:
    print(C[w])


image.png
# A=list(map(int,input().split()))
# B=list(set(A))
# B.sort()
# C={}
# for i in range(len(B)): C[B[i]]=i
# for w in A: print(C[w],end=' ')