import sys

list = []
K = int(input())

for _ in range(K):
    num = int(sys.stdin.readline())
    if num != 0:
        list.append(num)
    else:
        list.pop()
print(sum(list))


