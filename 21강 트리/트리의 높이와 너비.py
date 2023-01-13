

# import sys
# from collections import deque
# input = sys.stdin.readline
# n = int(input())
# lc = {i:0 for i in range(1,n+1)}
# rc = {i:0 for i in range(1,n+1)}
# lvl = {i:0 for i in range(1,n+1)}
# findroot = set(i for i in range(1,n+1))
# cntson ={i:[0,0] for i in range(1,n+1)}
# xpos= {i:0 for i in range(1+n+1)}

# for _ in range(n):
#     c,l,r = map(int,input().split())
#     lc[c] = l
#     rc[c] = r
#     findroot.discard(l)
#     findroot.discard(r)
# root = findroot.pop()

# def dfs(cur):
#     if lc[cur] != -1:
#         cntson[cur][0] += dfs(lc[cur])
#     if rc[cur] != -1:
#         cntson[cur][1] += dfs(rc[cur])
    
#     return sum(cntson[cur])+1

# dfs(root)


# # lvl = {i:[] for i in range(1,n+1)}  #각각 레벨은 필요없고 특정레벨에 들어와있는 노드들이 필요
# # 쉽지않음 lvl을 주는게 부모노드를 참고해야되는데 부모노드가 lvl값을 가지고 있지 않으면..
# q = deque([root])
# lvl[root] = 1
# lenlvl = 1
# while q:
#     cur = q.popleft()
#     for i, dir in enumerate([lc[cur],rc[cur]]):
#         if dir!=-1:
#             xpos[dir] = xpos[cur] - cntson[dir][1]-1 if i==0 else xpos[cur] + cntson[dir][0]+1 
#             lvl[dir] = lvl[cur]+1
#             lenlvl = lvl[dir]
#             q.append(dir)
            

# #걍 일일히 전 노드 확인해야될듯
# maxdis = 0
# maxlvl = 0
# level = [[] for _ in range(lenlvl+1)]
# for i in range(1,n+1):
#     level[lvl[i]].append(xpos[i])   #xpos값을 레벨별로 모아놓은 리스트

# for i in range(1,lenlvl+1):
#     curmaxdis = max(level[i]) - min(level[i]) + 1
#     if maxdis < curmaxdis:
#         maxdis = curmaxdis
#         maxlvl = i
# print(maxlvl,maxdis)


# # 그노드의 좌표값은 부모노드의 좌표값+ (lc로왓으면 +현노드의 rc자식갯수) (rc로 왔으면 -현노드의 lc자식갯수로 결정됨)
# # 편의상 루트노드의 좌표값을 0으로 두고 계산하면 좋을듯, 어짜피 너비만 구하니까
# # level확인하는거는 bfs 쓰면 쉽게 될듯?
# # 자식 노드 갯수는 dfs쓰는게 쉬운데.. 시간제한 2초 노드갯수 10^4, O(N^2)까지도 되는거 보니 bfs로 레벨확인, dfs로 좌표확인 둘다 써도 O(N+N)이니 충분할듯
# # 루트를 먼저 찾아야됨


############################
#inorder(중위순회)를 구하는 문제였음    중위 순회 순서 == 그 좌표의 x값


import sys

input = sys.stdin.readline
n = int(input())
lc = {i:0 for i in range(1,n+1)}
rc = {i:0 for i in range(1,n+1)}
findroot = set(i for i in range(1,n+1))

for _ in range(n):
    c,l,r = map(int,input().split())
    lc[c] = l
    rc[c] = r
    findroot.discard(l)
    findroot.discard(r)
root = findroot.pop()

xpos=1
level = [[] for _ in range(n+1)]
def dfs(cur,lvl):
    global xpos
    
    if lc[cur] != -1: dfs(lc[cur],lvl+1)
    level[lvl].append(xpos)
    xpos += 1
    if rc[cur] != -1: dfs(rc[cur],lvl+1)

dfs(root,1)

maxlvl = 1
maxdis = 1
for i in range(1,n+1):
    if not level[i]: break
    curmaxdis = max(level[i]) - min(level[i]) + 1
    if maxdis < curmaxdis:
        maxdis = curmaxdis
        maxlvl = i

print(maxlvl,maxdis)