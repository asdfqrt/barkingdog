import sys
board = []
cnt = [0,0]
n = int(input())
for _ in range(n):
    board.append(list(map(int,sys.stdin.readline().split())))

def check(x,y,n):
    for i in range(x,x+n):
        for j in range(y,y+n):
            if board[i][j] != board[x][y]: return False
    return True


def solve(x,y,n):
    if check(x,y,n):
        cnt[board[x][y]] += 1
        return
    z = int(n/2)
    for i in range(2):
        for j in range(2):
            solve(x+i*z,y+j*z,z)


solve(0,0,n)
print(*cnt,sep="\n")
    

