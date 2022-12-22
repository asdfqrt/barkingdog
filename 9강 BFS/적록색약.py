import sys
from collections import deque


N = int(input())
board = []
vis = [[False for _ in range(N)] for _ in range(N)]
Q = deque([])
dx= [1,0,-1,0]
dy= [0,1,0,-1]
num = [0,0]

for _ in range(N):
    board.append(sys.stdin.readline().rstrip())

def bfs(x,y):
    vis[x][y] = True
    Q.append([x,y])
    while Q:
        x,y = Q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0<=nx<N and 0<=ny<N and not vis[nx][ny] and board[nx][ny] == board[x][y]:
                vis[nx][ny] = True
                Q.append([nx,ny])


for i in range(N):
    for j in range(N):
        if not vis[i][j]:
            bfs(i,j)
            num[0] += 1

vis = [[False for _ in range(N)] for _ in range(N)]

def bfs_a(x,y):
    vis[x][y] = True
    Q.append([x,y])
    while Q:
        x,y = Q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0<=nx<N and 0<=ny<N and not vis[nx][ny] and (board[nx][ny] == board[x][y] or (board[nx][ny] != "B" and board[x][y] != "B")):
                vis[nx][ny] = True
                Q.append([nx,ny])

for i in range(N):
    for j in range(N):
        if not vis[i][j]:
            bfs_a(i,j)
            num[1] += 1

print(*num)
