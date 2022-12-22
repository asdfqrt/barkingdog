def func(n,r,c):
    if n==0: return 0
    half = 2**(n-1)
    if r<half and c<half: return func(n-1,r,c)
    elif r<half and c>=half: return half**2 + func(n-1,r,c-half)
    elif r>=half and c<half: return 2*(half**2) + func(n-1,r-half,c)
    else: return 3*(half**2) + func(n-1,r-half,c-half)

n,r,c = map(int,input().split())
print(func(n,r,c))