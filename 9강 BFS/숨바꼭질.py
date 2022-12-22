# from collections import deque

# Q= deque([])
# N,K = map(int,input().split())
# vis = [-1 for _ in range(100001)]
# Q.append(N)
# vis[N] = 0
# stop = True

# while Q and stop:

#     x = Q.popleft()
#     if x == K:
#         ans = vis[x]
#         stop = False

#     nx = x+1
#     if 0 <= nx <= 100000 and vis[nx] == -1:
#         vis[nx] = vis[x] +1
#         Q.append(nx)

#     nx = x-1
#     if 0 <= nx <= 100000 and vis[nx] == -1:
#         vis[nx] = vis[x] +1
#         Q.append(nx)

#     nx = 2*x
#     if 0 <= nx <= 100000 and vis[nx] == -1:
#         vis[nx] = vis[x] +1
#         Q.append(nx)

# print(ans)

from collections import deque

Q= deque([])
N,K = map(int,input().split())
vis = [-1 for _ in range(100001)]
Q.append(N)
vis[N] = 0


while Q:

    x = Q.popleft()
    if x == K:
        ans = vis[x]
        break

    for nx in [x-1,x+1, 2*x]:
        if 0 <= nx <= 100000 and vis[nx] == -1:
            vis[nx] = vis[x] +1
            Q.append(nx)

print(ans)