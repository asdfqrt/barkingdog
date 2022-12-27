import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = {}

for _ in range(n):
    site, pwd = input().split()
    arr[site] = pwd
for _ in range(m):
    print(arr[input().rstrip()])

