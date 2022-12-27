import sys
input= sys.stdin.readline
n=int(input())
arr = set()
for _ in range(n):
    name, order = input().split()
    if order=="enter":
        arr.add(name)
    else:
        arr.remove(name)
print(*sorted(list(arr))[::-1], sep="\n")
