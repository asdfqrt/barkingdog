# import sys
# import math
# def check(board):
#     for i in range(len(board)):
#         for j in range(len(board)):
#             if board[i][j] != board[0][0]: return False
#     return True


# def paper(k,board,numm,numz,nump):
#     # if k== 0:
#     #     if board[0][0] == -1: return numm+1,numz,nump
#     #     elif board[0][0] == 0: return numm,numz+1,nump
#     #     else: return numm,numz,nump+1
#     if check(board):
#         if board[0][0] == -1: return numm+1,numz,nump
#         elif board[0][0] == 0: return numm,numz+1,nump
#         else: return numm,numz,nump+1

#     else:
#         numm_sum = 0
#         numz_sum = 0
#         nump_sum = 0
#         for i in range(3):
#             for j in range(3):
#                 m,z,p = paper(k-1,slicing(k,i,j,board),numm,numz,nump)
#                 numm_sum += m
#                 numz_sum += z
#                 nump_sum += p
#         return numm_sum,numz_sum,nump_sum



# def slicing(k,i,j,board):
#     new_board = []
#     for xpos in range(i*3**(k-1),(i+1)*3**(k-1)):
#         new_board.append(board[xpos][j*3**(k-1):(j+1)*3**(k-1)])
#     return new_board




# board =[]
# n = int(input())
# k = int(math.log(n,3))

# for i in range(n):
#     board.append(list(map(int,sys.stdin.readline().split())))


# print(*paper(k,board,0,0,0),sep="\n")

import sys

board =[]
cnt = [0,0,0]

n = int(input())
for i in range(n):
    board.append(list(map(int,sys.stdin.readline().split())))

def check(x,y,n):
    for i in range(x,x+n):
        for j in range(y,y+n):
            if board[x][y] != board[i][j]:
                return False
    return True

def solve(x,y,z):
    if check(x,y,z):
        cnt[board[x][y]+1] += 1
        return
    n = int(z/3)
    for i in range(3):
        for j in range(3):
            solve(x+i*n,y+j*n,n)

solve(0,0,n)
print(*cnt,sep="\n")