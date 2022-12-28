#이동은 bfs에서하던대로 하면될듯
#10x10행렬에 확인해야되는 문자열k는 10^3개이므로 O(N^2)까지도 가능인데 아마 O(N)에풀릴듯

# import sys
# from collections import deque

# input= sys.stdin.readline
# dx=[1,0,-1,0,1,1,-1,-1]
# dy=[0,1,0,-1,1,-1,1,-1]
# n,m,k = map(int,input().split())
# arr=[]
# likedic={}
# likelen=0
# for _ in range(n):
#     arr.append(input().rstrip())
# for _ in range(k):
#     like = input().rstrip()
#     likelen=max(likelen,len(like))
#     likedic[like] = 0
        
# def solve(x,y,string):
#     string += arr[x][y]
#     if string in likedic:
#         likedic[string] += 1
#     if len(string) < likelen:
#         for dir in range(8):
#             nx = x + dx[dir] 
#             ny = y + dy[dir]
#             if nx == -1: nx = n-1   #n,m이 3보다 크므로 대각선이 반대 대각선이랑 겹치는 경우 나오지 않음
#             elif nx == n: nx = 0
#             if ny == -1: ny = m-1
#             elif ny == m: ny = 0
#             solve(nx,ny,string)
#     else: return


# for x in range(n):
#     for y in range(m):
#         solve(x,y,"")
# print(*likedic.values(), sep="\n")




import sys
input= sys.stdin.readline
dx=[1,0,-1,0,1,1,-1,-1]
dy=[0,1,0,-1,1,-1,1,-1]
n,m,k = map(int,input().split())
arr=[]
likedic={}
likelen=0
likelist=[]
for _ in range(n):
    arr.append(input().rstrip())
for _ in range(k):
    like = input().rstrip()
    likelen=max(likelen,len(like))
    likedic[like] = 0
    likelist.append(like)

def solve(x,y,string):
    string += arr[x][y] #하다보니 굳이 큐가 없어도 되서 뺐음
    if string in likedic:
        likedic[string] += 1
    if len(string) < likelen:
        for dir in range(8):    #n,m이 3보다 크므로 대각선이 반대 대각선이랑 겹치는 경우 나오지 않음
                nx = (x + dx[dir] + n) % n
                ny = (y + dy[dir] + m) % m
                solve(nx,ny,string)
    else: return

for x in range(n):
    for y in range(m):
        solve(x,y,"")
for i in likelist:  #이거 없으면 중복된 신이 좋아하는 문자열에 대해서는 갯수 출력이 안됨
    print(likedic[i])
