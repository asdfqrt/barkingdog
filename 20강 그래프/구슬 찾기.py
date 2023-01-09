# # 중간이 될 수있는 조건? 3개 이상일때 양 끝 값이 아니고
# # ex 9<  .... < 10이고 {5,6,7}, {2,3,4} 집단 둘이 사이에 드가고 저 집단간 대소관계 파악을 못하더라도 중간 값은 7또는 4밖에 될수없다
# # 9<5<6<7 <2<3<4<10 또는 9<2<3<4 <5<6<7<10 임
# # 문제에 힌트가 있는듯
# # 1번 구슬과 4번 구슬은 무게가 중간인 구슬이 절대 될 수 없다는 것은 확실히 알 수 있다. 1번 구슬보다 무거운 것이 2, 4, 5번 구슬이고, 4번 보다 가벼운 것이 1, 2, 3번이다 
# # 1개 노드에서 따라가서 대소관계를 알 수 있는 노드의 갯수가 절반갯수를 넘으면 안되나봄 
# # 5개 노드중 3개 이상이 자기보다 크다 or 작다가 나오니까 문제 된 것
# # 방향 그래프는 안됨, 간선자체는 연결되어 있되 어느쪽이 큰지 알려야됨, 마이너스 노드를 만들어서 거기 연결하면될듯?
# # ㄴㄴ 아예 n^n adj를 만들어서 무거운 연결은 1 가벼운 연결은 -1 식으로 하는게 나을듯
# import sys
# input= sys.stdin.readline
# n,m = map(int,input().split())
# adj = [[0]*n for _ in range(n)]

# for _ in range(m):
#     a,b = map(int,input().split())
#     adj[a-1][b-1] = 1
#     adj[b-1][a-1] = -1

# pos_vis = [False]*n
# neg_vis = [False]*n

# def pos_dfs(st,en,dep):
#     if st == en: return 0
#     if adj[st][en] < 0: return dep #만약 a -> b가 b가 더 크다면 여기까지의 깊이 반환
#     if pos_vis[st]: return adj[st][en]    #만약 st을 다뤄서 비교한적이 있으면 기록되어있는 깊이 반환 >> 애매한데 아니다 사이클을 이룰수가 없으니까 애매하지않음
#     pos_vis[st] = True

#     max_depth = dep
#     for dir in range(n):
#         if not pos_vis[dir]:
#                 max_depth=max(max_depth,pos_dfs(dir,en,dep+1))
#     adj[st][en] = max_depth    #memoization            
#     return max_depth




# def neg_dfs(st,en,dep):
#     if st == en: return 0
#     if adj[st][en] > 0: return dep
#     if neg_vis[st]: return adj[st][en]
#     neg_vis[st] = True
#     min_depth = dep
#     for dir in range(n):
#         if not neg_vis[dir]:
#                 min_depth=min(min_depth,neg_dfs(dir,en,dep-1))
#     adj[st][en] = min_depth            
#     return min_depth

# def check(st,en,n):
#     mid = (n+1)//2
#     if pos_dfs(st,en,0) > mid or neg_dfs(st,en,0) < -mid:
#         return False
#     return True

# cnt = 0 #모든 구슬은 대소관계에 있으나 다 연결안되있을수있으니 시작점 따로
# for st in range(n):
#     for en in range(n):
#         if not check(st,en,n+1):
#             cnt += 1

# print(cnt)




import sys
input = sys.stdin.readline
n,m = map(int,input().split())
b2s = [[] for _ in range(n)]
s2b = [[] for _ in range(n)]

vis = [False]*n
for _ in range(m):
    big,small = map(int,input().split())
    b2s[big-1].append(small-1)
    s2b[small-1].append(big-1)


def solve(bead,n):
    global vis
    global hv
    global lt
    mid = (n+1)//2
    vis = [False]*n
    hv = 0
    pos_dfs(bead)
    if hv >= mid: return False
    vis = [False]*n
    lt = 0
    neg_dfs(bead)
    if lt >= mid: return False
    return True

def pos_dfs(cur):   #메모이제이션 하려면 내 뒤로 몇개 더있냐를 표시해야되는데 그걸 표시하기가 힘든듯
    vis[cur] = True
    global hv
    for dir in s2b[cur]:
        if not vis[dir]:
            pos_dfs(dir)
            hv +=1
    

def neg_dfs(cur):
    vis[cur] = True
    global lt
    for dir in b2s[cur]:
        if not vis[dir]:
            neg_dfs(dir)
            lt +=1

cnt = 0
for bead in range(n):
    if not solve(bead,n): cnt +=1
print(cnt)

