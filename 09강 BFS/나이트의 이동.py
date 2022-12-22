from collections import deque
N = int(input())
dx = [2,2,1,1,-1,-1,-2,-2]
dy = [1,-1,2,-2,2,-2,1,-1]


def bfs(x,y,destx,desty):
    vis[x][y] = True
    Q.append([x,y])
    while Q:
        x,y = Q.popleft()
        if destx == x and desty == y:
            print(dis[x][y])
            break
        for dir in range(8):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < I and 0 <= ny < I and not vis[nx][ny]:
                vis[nx][ny] = True
                dis[nx][ny] = dis[x][y] + 1
                Q.append([nx,ny])

for i in range(N):
    I = int(input())
    Q = deque([])
    vis = [[False for _ in range(I)] for _ in range(I)]
    dis = [[0 for _ in range(I)] for _ in range(I)]
    x,y = map(int,input().split())
    destx,desty = map(int,input().split())
    bfs(x,y,destx,desty)
