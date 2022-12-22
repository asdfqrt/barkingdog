import sys
from collections import deque

x = sys.stdin.readline().rstrip()
stack = 0
list = deque([])
laser = False

for i in x:
    if i == "(":
        list.append("(")
        laser = True
 
    else:
        list.pop()
        if laser:
            stack += len(list)
        else:
            stack += 1
        laser = False

print(stack)

