# 주어진 그래프를 트리로 만들기
# 두 뉴런 사이에는 최대 1개의 시냅스만 존재한다. >> 애초부터 최대 한개의 연결??? 그럼 끊을 필요가 있나?? 1-2-3-4-1-2.... 한개라도 사이클가능

# import sys
# input= sys.stdin.readline
# sys.setrecursionlimit(10**6)
# n,m = map(int,input().split())
# adj = {i+1:[] for i in range(n)}
# for _ in range(m):
#     a,b = map(int,input().split())
#     adj[a] += [b]
#     adj[b] += [a]
# p = [0]* (n+1)

# # 트리 = 사이클이 없는 그래프니까 사이클을 끊어내면 될거 같은데 어느 시점에서 끊어내느냐가 문제인듯?
# # 잘 모르겠으니까 일단 사이클이 발생한 시점 = 왔던곳 또 온시점에서 끊어보기
# # 이전에 이 끊은 사이클 지나간 놈들은 어떡함? 그런일 없을듯? dfs돌리면 사이클이 제일 첫 트라이에 찾아질듯

# # 남은건 트리의 갯수 구해서 그냥 더하면 될듯 > 트리의 갯수를 구하려면 p를 리스트로 따로 떼서 보관해둬야됨 p[0]이 아니면 사이클
# # 트리두개 > 더하기 1번, 트리 x개 > 더하기 x-1번
# # 1) 사이클을 끊어 트리만들고 2) 트리갯수를 구하기

# cycle = set()
# cut = 0
# def break_cycle(cur,p):
#     global cut
#     if cur in cycle:
#         adj[cur].remove(p)
#         adj[p].remove(cur)
#         cut +=1
#         return
#     cycle.add(cur)
#     for dir in adj[cur]:
#         if dir != p:
#             break_cycle(dir,cur)
#     cycle.remove(cur)

# def count_tree(cur):
#     for dir in adj[cur]:
#         if dir != p[cur]:
#             if p[dir] == 0:
#                 p[dir] = cur
#                 count_tree(dir)



# for i in range(1,n+1):
#     break_cycle(i,0)

# cnt = 0
# for i in range(1,n+1):
#     if p[i] == 0:
#         cnt+=1
#         count_tree(i)
# print(cut+cnt-1)


# TLE남
# 아마 사이클을 끊고 세는걸 한번에 해야되는듯

#########################################

import sys
input= sys.stdin.readline
sys.setrecursionlimit(10**6)
n,m = map(int,input().split())
adj = {i+1:[] for i in range(n)}
for _ in range(m):
    a,b = map(int,input().split())
    adj[a] += [b]
    adj[b] += [a]
p = [0]* (n+1)

def count_tree(cur):
    for dir in adj[cur]:
        if dir != p[cur]:
            if p[dir] == 0:
                p[dir] = cur
                count_tree(dir)

cnt = 0
for i in range(1,n+1):
    if p[i] == 0:
        cnt+=1
        count_tree(i)

print((cnt-1) + (m+cnt-1) -(n-1))
# 실제로 사이클을 끊고 잇는게 아니라
# 1) 트리는 n-1개의 간선을 가진다
# 3) 시냅스 그래프의 간선 숫자를 n-1개로 줄이면, 모든 노드는 한번씩만 연결된다 = 간선 갯수만 맞추면 무조건 트리가 된다x 다른 그래프로 분리되어 버릴수도 있음. 트리가 될수있는 최소 요건
# 3) 서로다른 x개 트리는 x-1개의 간선으로 하나의 트리로 연결된다
# 를 사용함

# 연결그래프의 갯수를 세면 cnt개가 나오는데 cnt-1개의 간선으로 하나의 그래프로 만들수있음
# 이때 총 간선의 갯수는 기존의 m개 + 새로그은 cnt-1개인데 실제 그래프의 노드는 n개이기에 트리가 되려면 간선이 n-1까지 줄어들어야됨
# 즉 잘라내야 하는 간선의 갯수는 (m+cnt-1) - (n-1)개
# 최종연산은 (cnt-1) + (m+cnt-1) -(n-1)
