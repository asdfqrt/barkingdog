from collections import deque

R,C = map(int,input().split())
board = []
Q_J = deque([])
Q_F = deque([])
dist_j = [[-1 for _ in range(C)] for _ in range(R)]
dist_f = [[-1 for _ in range(C)] for _ in range(R)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]
nofire = True

for i in range(R):
    x= input()
    board.append(x)
    if "J" in x:
        j = x.index("J")
        Q_J.append([i,j])
        dist_j[i][j] = 0
    if "F" in x:
        j = x.index("F")
        Q_F.append([i,j])
        dist_f[i][j] = 0

        nofire = False
if nofire:
    dist_f = [[1000*1000 for _ in range(C)] for _ in range(R)]

while Q_F:
    x,y = Q_F.popleft()
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] != "#" and dist_f[nx][ny] == -1:
            dist_f[nx][ny] = dist_f[x][y] + 1
            Q_F.append([nx,ny])

stop = True
ans = -1
while Q_J and stop:
    x,y = Q_J.popleft()
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            ans = dist_j[x][y]+1
            stop = False
            break
        elif board[nx][ny] != "#" and dist_f[nx][ny] > dist_j[x][y]+1 and dist_j[nx][ny] == -1:
            dist_j[nx][ny] = dist_j[x][y] + 1
            Q_J.append([nx,ny])


if ans == -1:
    print("IMPOSSIBLE")
else:
    print(ans)


