def func(n):
    if n == 0:
        return
    print(n)
    func(n-1)

func(9)

def func1(n):
    if n==0:
        return 0
    return n+func1(n-1)

func1(9)