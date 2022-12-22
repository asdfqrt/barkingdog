# import sys
# N = int(input())
# list = []
# head = 0
# tail = 0

# for _ in range(N):
#     cmd = sys.stdin.readline().rstrip()
#     if cmd == "pop":
#         if head != tail:
#             print(list[head])
#             head += 1
#         else:
#             print(-1)
            

#     elif cmd == "size":
#         print(tail-head)


#     elif cmd == "empty":
#         if head == tail:
#             print(1)
#         else:
#             print(0)
#     elif cmd == "front":
#         if head != tail:
#             print(list[head])
#         else:
#             print(-1)
#     elif cmd == "back":
#         if head != tail:
#             print(list[tail-1])
#         else:
#             print(-1)
#     else:
#         list.append(cmd[5:])
#         tail += 1

from collections import deque
import sys


n = int(sys.stdin.readline())
q = deque([])
    
for _ in range(n):
    word = sys.stdin.readline().split()
    if word[0] == 'pop':
        print(q.popleft() if q else -1)
    elif word[0] == 'size':
        print(len(q))
    elif word[0] == 'empty':
        print(0 if q else 1)
    elif word[0] == 'front':
        print(q[0] if q else -1)
    elif word[0] == 'back':
        print(q[-1] if q else -1)
    else:
        q.append(int(word[1]))