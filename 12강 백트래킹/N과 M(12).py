from itertools import combinations_with_replacement
n,m = map(int, input().split())
arr = list(map(int,input().split()))
arr.sort()
for i in sorted(set(combinations_with_replacement(arr,m))):
    print(*i)