import sys
from collections import deque

N = int(input())
cnt = 0

for i in range(N):
    x = sys.stdin.readline().rstrip()
    list = deque([])
    for j in x:
        if j == "A":
            try:
                if list.pop() != "A":
                    list.append("B")
                    list.append("A")
            except:
                list.append("A")
        if j == "B":
            try:
                if list.pop() != "B":
                    list.append("A")
                    list.append("B")
            except:
                list.append("B")

    if len(list) == 0:
        cnt += 1

print(cnt)


