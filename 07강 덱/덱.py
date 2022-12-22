# from collections import deque
# import sys

# q = deque([])
# N = int(input())

# for _ in range(N):
#     cmd = sys.stdin.readline().split()
#     if cmd[0] == "push_front":
#         q.appendleft(cmd[1])
#     if cmd[0] == "push_back":
#         q.append(cmd[1])
#     if cmd[0] == "pop_front":
#         try:
#             print(q.popleft())
#         except:
#             print(-1)
#     if cmd[0] == "pop_back":
#         try:
#             print(q.pop())
#         except:
#             print(-1)

#     if cmd[0] == "size":
#         print(len(q))
#     if cmd[0] == "empty":
#         print(0 if q else 1)
#     if cmd[0] == "front":
#         try:
#             tmp = q.popleft()
#             print(tmp)
#             q.appendleft(tmp)
#         except:
#             print(-1)
#     if cmd[0] == "back":
#         try:
#             tmp = q.pop()
#             print(tmp)
#             q.append(tmp)
#         except:
#             print(-1)


from collections import deque
import sys

q = deque([])
N = int(input())

for _ in range(N):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push_front":
        q.appendleft(cmd[1])
    if cmd[0] == "push_back":
        q.append(cmd[1])
    if cmd[0] == "pop_front":
        print(q.popleft() if q else -1)
    if cmd[0] == "pop_back":
        print(q.pop() if q else -1)
    if cmd[0] == "size":
        print(len(q))
    if cmd[0] == "empty":
        print(0 if q else 1)
    if cmd[0] == "front":
        print(q[0] if q else -1)
    if cmd[0] == "back":
        print(q[-1] if q else -1)