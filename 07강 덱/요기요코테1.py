
from collections import deque
q = deque([])
def solution(stack1, stack2, stack3):
    # write your code in Python 3.8.10
    whole = stack1+stack2+stack3
    whole.sort(reverse=True)
    for x in whole:
        if x in stack1:
            q.append("1")
        elif x in stack2:
            q.append("2")
        else:
            q.append("3")
    return "".join(q)

stack1 = [7]
stack2 = []
stack3 = [31]

print(solution(stack1, stack2, stack3))