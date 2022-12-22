# import sys
# from collections import deque
# N = int(input())
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]

# def bfs_f():
#     while Q_f:
#         x,y = Q_f.popleft()
#         for dir in range(4):
#             nx = x + dx[dir]
#             ny = y + dy[dir]
#             if 0 <= nx < h and 0 <= ny < w and board[nx][ny] != "#" and dis_f[nx][ny] == w*h:
#                 dis_f[nx][ny] = dis_f[x][y] + 1
#                 Q_f.append([nx,ny])

# def bfs_s():
#     while Q_s:
#         x,y = Q_s.popleft()
#         for dir in range(4):
#             nx = x + dx[dir]
#             ny = y + dy[dir]
#             if nx < 0 or nx >= h or ny < 0 or ny >= w:
#                 ans = dis_s[x][y]+1
#                 print(ans)
#                 return

#             elif board[nx][ny] != "#" and dis_f[nx][ny] > dis_s[x][y]+1 and dis_s[nx][ny] == -1:
#                 dis_s[nx][ny] = dis_s[x][y] + 1
#                 Q_s.append([nx,ny])
#     print("IMPOSSIBLE")


# for i in range(N):
#     w,h = map(int,input().split())
#     board = []
#     Q_s = deque([])
#     Q_f = deque([])
#     dis_s = [[-1 for _ in range(w)] for _ in range(h)]
#     dis_f = [[w*h for _ in range(w)] for _ in range(h)]

#     for i in range(h):
#         x= sys.stdin.readline().rstrip()
#         board.append(x)
#         for j in range(w):
#             if board[i][j] =="@":
#                 Q_s.append([i,j])
#                 dis_s[i][j] = 0
#             elif board[i][j] == "*":
#                 Q_f.append([i,j])
#                 dis_f[i][j] = 0
    
#     bfs_f()
#     bfs_s()

import sys
from collections import deque
N = int(input())
dx = [1,0,-1,0]
dy = [0,1,0,-1]
INF = sys.maxsize

def bfs():
    w,h = map(int,input().split())
    board = []
    Q= deque([])
    dist = [[INF]*w for _ in range(h)]

    for i in range(h):
        board.append(sys.stdin.readline().rstrip())
        for j in range(w):
            if board[i][j] =="@":
                Q.append([i,j,"s"])
                dist[i][j] = 0
            elif board[i][j] == "*":
                Q.append([i,j,"f"])
                dist[i][j] = 0

    while Q:
        x,y,what = Q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                if what == "s":
                    print(dist[x][y])
                    return
            elif board[nx][ny] != "#" and dist[nx][ny] > dist[x][y]:
                dist[nx][ny] = dist[x][y] +1
                Q.append([nx,ny,what])
    print("IMPOSSIBLE")


for i in range(N):
    bfs()