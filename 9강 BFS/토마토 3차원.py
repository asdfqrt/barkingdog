import sys
from collections import deque
Q = deque([])
dx = [0,1,0,-1,0,0]
dy = [1,0,-1,0,0,0]
dz = [0,0,0,0,1,-1]
M,N,H = map(int,sys.stdin.readline().rstrip().split())
board = [[] for _ in range(H)]
maxvalue = 0 #dis값을 추가하면 걍 시간초과 떠버림


for h in range(H):
    for n in range(N):
        board[h].append(list(map(int,sys.stdin.readline().rstrip().split())))
        for m in range(M):
            if board[h][n][m] == 1:
                Q.append([h,n,m])

while Q:
    z,x,y = Q.popleft()
    for dir in range(6):
        nz= z + dz[dir]
        nx= x + dx[dir]
        ny= y + dy[dir]
        if 0<=nz<H and 0<=nx<N and 0<=ny<M and board[nz][nx][ny] == 0:
            Q.append([nz,nx,ny])
            board[nz][nx][ny] = board[z][x][y] +1

for h in range(H):
    for n in range(N):
        for m in range(M):
            if board[h][n][m] == 0:
                print(-1)
                sys.exit()
            maxvalue = max(maxvalue, board[h][n][m])

print(maxvalue-1)


