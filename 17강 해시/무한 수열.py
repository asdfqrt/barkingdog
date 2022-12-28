#n이 10^12, p,q,가 최소인 경우 피보나치처럼 개오래 걸릴수있다

n,p,q = map(int,input().split())
memoization = {0:1}
def func(i):
    if i not in memoization:
        memoization[i] =  func(i//p) + func(i//q)
    return memoization[i]

print(func(n))
