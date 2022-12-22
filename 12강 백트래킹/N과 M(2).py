# from itertools import combinations

# n,m = map(int,input().split())
# arr = [i+1 for i in range(n)]
# for i in combinations(arr,m):
#     print(*i)



from itertools import combinations
n,m = map(int, input().split())
for i in combinations(range(1,n+1),m):
    print(*i)