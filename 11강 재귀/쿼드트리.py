# import sys
# n = int(input())
# board = []
# res = ""
# for _ in range(n):
#     board.append(sys.stdin.readline().rstrip())

# def check(x,y,n):
#     for i in range(x,x+n):
#         for j in range(y,y+n):
#             if board[x][y] != board[i][j]: return False
#     return True

# def solve(x,y,n,res):
#     if check(x,y,n):
#         res = res + board[x][y]
#         return res
#     else:
#         res = res + "("
#         z = int(n/2)
#         for i in range(2):
#             for j in range(2):
#                 res = solve(x+i*z,y+j*z,z,res)
#         res = res + ")"
#         return res

# print(solve(0,0,n,res))


def paper(x, y, N):
    N //= 2
    
    if N == 0:
        return arr[x][y]
    
    Q1 = paper(x, y, N)
    Q2 = paper(x, y+N, N)
    Q3 = paper(x+N, y, N)
    Q4 = paper(x+N, y+N, N)

    if (Q1 in ['0', '1']) and Q1 == Q2 == Q3 == Q4:
        return Q1
    
    return '(' + Q1 + Q2 + Q3 + Q4 + ')'

N = int(input()) # 한 변의 길이 N 입력받기
arr = [input() for _ in range(N)]

Q = paper(0, 0, N)

print(Q)