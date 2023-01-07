# # 매번 dfs로 탐색가능인지 확인하는건 구질거 같고
# # d[출발][도착] 으로 표시 해놓는게 좋을듯? >> 이게 그냥 adj[출발][도착] 이네
# # dfs 해도 자기한테 시작해도 도착하수잇어야 1임


import sys
input =sys.stdin.readline

n = int(input())
adj = []

for i in range(n):
    adj.append(list(map(int,input().split())))

def check(st,en):
    vis[st] = True
    if adj[st][en]: return True
    for dir in range(n):
        if adj[st][dir] and not vis[dir] and check(dir,en):
            adj[dir][en] = 1        #memoization
            return True
    return False


for i in range(n):
    for j in range(n):
        vis = [False] * n
        print(1 if check(i,j) else 0, end = " ")
    print()
