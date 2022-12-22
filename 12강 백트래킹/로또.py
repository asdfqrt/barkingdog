from itertools import combinations
cnt = 0
arr = []
while True:
    ks = list(map(int, input().split()))
    if ks[0] == 0:
        break
    arr.append(ks[1:])
    cnt += 1

for i in range(cnt):
    for j in sorted((combinations(arr[i],6))):
        print(*j)
    print("")


