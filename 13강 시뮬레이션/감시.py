import copy

n,m = map(int,input().split())
board=[]
ctype=[]
cpos=[]
wpos=[]
for i in range(n):
    board.append(list(map(int,input().split())))
    for j in range(len(board[i])):
        type = board[i][j]
        if type!=0:
            if type==6:
                wpos.append([i,j])
            else:
                ctype.append(type)
                cpos.append([i,j])

spin=[0 for _ in range(len(ctype))]

