def dfs(x,y):
    vis[x][y] = True
    for dir in range(8):
        dx = x + nx[dir]
        dy = y + ny[dir]
        if 0<=dx<h and 0<=dy<w and array[dx][dy]==1 and not vis[dx][dy]:
            dfs(dx,dy)

import sys
input =sys.stdin.readline
sys.setrecursionlimit(10**6)
nx = [1,0,-1,0,1,1,-1,-1]
ny = [0,1,0,-1,1,-1,1,-1]

while True:
    w,h = map(int,input().split())
    if w==0 and h==0: exit()
    array = []
    vis = [[False]*w for _ in range(h)]
    cnt = 0
    for _ in range(h):
        array.append(list(map(int,input().split())))
    for x in range(h):
        for y in range(w):
            if array[x][y]==1 and not vis[x][y]:
                dfs(x,y)
                cnt +=1
    print(cnt)