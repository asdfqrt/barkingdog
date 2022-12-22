import sys
from collections import deque

while True:
    x = sys.stdin.readline().rstrip()
    if x == ".":
        break

    answer = "yes"
    list = deque([])

    for i in x:
        if i == "[":
            list.append("[")
        elif i == "(":
            list.append("(")
        elif i == "]":
            try:
                if list.pop() != "[":
                    answer = "no"
            except:
                answer = "no"
        elif i == ")":
            try: 
                if list.pop() != "(":
                    answer = "no"
            except:
                answer = "no"
    

    if len(list) != 0:
        answer = "no"
    print(answer)
