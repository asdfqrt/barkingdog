import sys
from collections import deque

N,M = map(int, input().split())
board = []
dis = [[-1 for _ in range(M)] for _ in range(N)]
Q = deque([])
dx = [1,0,-1,0]
dy = [0,1,0,-1]


for i in range(N):
    board.append(list(sys.stdin.readline().rstrip()))

Q.append([0,0])
dis[0][0] = 0

while Q:
    cur = Q.popleft()
    if cur == [N-1,M-1]: break

    for dir in range(4):
        nx = cur[0] + dx[dir]
        ny = cur[1] + dy[dir]

        # if nx < 0 or nx >= N or ny <0 or ny >= M: continue
        # if board[nx][ny] == "0" or dis[nx][ny] != -1: continue

        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == "1" and dis[nx][ny] == -1:
        
            dis[nx][ny] = dis[cur[0]][cur[1]] + 1
            Q.append([nx,ny])

print(dis[N-1][M-1]+1)

