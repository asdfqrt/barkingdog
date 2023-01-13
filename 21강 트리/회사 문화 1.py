#만약 직속상사의 번호가 -1 1 1 1 3 로 주어진다면
# 사장 한명 아래에 직속 부하 3명이있고 3번직원 밑에 5번직원이 있는것
# adj[숫자] = 차례
# 2초인데 매 시행마다 dfs해도 되겟지? n = 10^5, m=10^5 매 시행마다 전부 탐색하면 10^10? > TLE뜸
# 각 노드에 칭찬 값을 입력받아서 기다리고 있다가 입력이 끝나고 나면 루트에서(사장)부터 dfs를 한번만 돌려서 전달해보기 >> O(10^5)

def dfs(cur,fall):
    point[cur] += fall
    for dir in adj[cur]:
        dfs(dir,point[cur])

import sys
sys.setrecursionlimit(10**6)
input= sys.stdin.readline
n,m = map(int,input().split())
adj = {i:[] for i in range(1,n+1)}
point = {i:0 for i in range(1,n+1)}

for sub,worker in enumerate(map(int,input().split())):
    if sub==0: continue
    adj[worker].append(sub+1)


for _ in range(m):
    i,w = map(int,input().split())
    point[i] += w


dfs(1,0)
print(*point.values())


# def dfs(cur,w):
#     point[cur] += w
#     for dir in adj[cur]:
#         dfs(dir,w)

# import sys
# sys.setrecursionlimit(10**6)
# input= sys.stdin.readline
# n,m = map(int,input().split())
# adj = {i:[] for i in range(1,n+1)}
# point = {i:0 for i in range(1,n+1)}

# for sub,worker in enumerate(map(int,input().split())):
#     if sub==0: continue
#     adj[worker].append(sub+1)


# for _ in range(m):
#     i,w = map(int,input().split())
#     dfs(i,w)

# print(*point.values())



