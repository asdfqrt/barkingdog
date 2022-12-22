# from collections import deque

# T= int(input())
# num = [0] * T
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]

# for t in range(T):
#     M,N,K = map(int,input().split())
#     board = [[0 for _ in range(M)] for _ in range(N)]
#     vis = [[False for _ in range(M)] for _ in range(N)]



#     Q= deque([])


#     for _ in range(K):
#         X,Y = map(int,input().split())
#         board[Y][X] = 1

#     for i in range(N):
#         for j in range(M):
#             if board[i][j] == 1 and vis[i][j] == False:
#                 Q.append([i,j])
#                 vis[i][j] = True
#                 num[t] += 1
#                 while Q:
#                     x,y = Q.popleft()
#                     for dir in range(4):
#                         nx = x + dx[dir]
#                         ny = y + dy[dir]
#                         if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 1 and not vis[nx][ny]:
#                             vis[nx][ny] = True
#                             Q.append([nx,ny])
# print(*num,sep="\n")






from collections import deque

T= int(input())
num = [0] * T
dx = [1,0,-1,0]
dy = [0,1,0,-1]


def bfs(x,y):
    vis[x][y] = True
    Q.append([x,y])
    while Q:
        x,y = Q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 1 and not vis[nx][ny]:
                vis[nx][ny] = True
                Q.append([nx,ny])


for t in range(T):
    M,N,K = map(int,input().split())
    board = [[0 for _ in range(M)] for _ in range(N)]
    vis = [[False for _ in range(M)] for _ in range(N)]



    Q= deque([])


    for _ in range(K):
        X,Y = map(int,input().split())
        board[Y][X] = 1

    for i in range(N):
        for j in range(M):
            if board[i][j] == 1 and not vis[i][j]:
                bfs(i,j)
                num[t] += 1
print(*num,sep="\n")







