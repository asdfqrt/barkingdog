cnt = 0
n = int(input())
isused1 = [False for _ in range(n)]
isused2 = [False for _ in range(2*n-1)]
isused3 = [False for _ in range(2*n-1)]


def func(cur):
    if cur==n:
        global cnt
        cnt += 1
        return


    for y in range(n):
        if not isused1[y] and not isused2[cur+y] and not isused3[cur-y+n-1]:
            isused1[y] = True
            isused2[cur+y] = True
            isused3[cur-y+n-1] = True
            func(cur+1)
            isused1[y] = False
            isused2[cur+y] = False
            isused3[cur-y+n-1] = False

func(0)
print(cnt)