import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = []
sarr = {}
for i in range(n):
    name = input().rstrip()
    arr.append(name)
    sarr[name] = i+1
for i in range(m):
    prob = input().rstrip()
    if prob in sarr:
        print(sarr[prob])
    else:
        print(arr[int(prob)-1])

