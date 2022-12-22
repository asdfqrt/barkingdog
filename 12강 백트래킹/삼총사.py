from itertools import combinations
result = 0
arr = list(map(int,input().split()))
arr.sort()
for i in combinations(arr,3):
    print(*i)
    if sum(i) == 0:
        result += 1
print(result)