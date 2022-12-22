from collections import deque

board = []
Q = deque([])
M,N = map(int,input().split())
dx = [1,0,-1,0]
dy = [0,1,0,-1]
dis = [[-1 for _ in range(M)] for _ in range(N)]
done = True
cnt = 0

for i in range(N):
    board.append(list(map(int,input().split())))

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            Q.append([i,j])
            dis[i][j] = 0
        if board[i][j] == 0:
            cnt += 1
            
            

while Q:
    cur = Q.popleft()
    for dir in range(4):
        nx = cur[0] + dx[dir]
        ny = cur[1] + dy[dir]
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0 and dis[nx][ny] == -1:
            dis[nx][ny] = dis[cur[0]][cur[1]] +1
            Q.append([nx,ny])
for i in range(N):
    for j in range(M):
        if dis[i][j] == -1 and board[i][j] == 0:
            done = False
            break

if cnt == 0:
    print(0)
elif not done:
    print(-1)
else:
    print(max(map(max,dis)))
