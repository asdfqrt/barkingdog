# 트리 조건 문제인듯
# 사이클이 없으면서 모두 방문하면 될듯
# cur에서 dir 확인시 cur자신을 제외하고는 전부 방문해 본적이 없는 장소만 나온다 + 모든 노드 확인이 가능하다 = Tree
# 가정이 틀림 주어지는 노드가 모두 연결된것이 아님, 아마 트리 한개있으면 루트 바꿔도 다 똑같은 트리로 보는듯

def dfs(cur):
    for dir in adj[cur]:
        if dir != p[cur]:   #경로 노드가 현재 노드의 부모가 아닐경우
            if p[dir] == 0:
                p[dir] = cur   #현재 노드의 자식에 넣어
                if not dfs(dir): return False
            else:
                return False    # dir에 다른 경로로 방문한적이 있으면 사이클
    return True

import sys
input= sys.stdin.readline
Case = []
while True:
    
    n,m = map(int,input().split())
    if n == 0 and m == 0: break
    Case.append(0)
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        adj[a].append(b)
        adj[b].append(a)

    p = [0]*(n+1)
    for i in range(1,n+1): #모든 노드에 대해 일일히 루트확인, 루트가 가능 = Tree>> 더 빠른 방법이 있지않을까?
        if p[i] == 0:
            if dfs(i): Case[-1] += 1

for i,T in enumerate(Case):
    if T>1:
        print("Case %d: A forest of %d trees." %((i+1),T))
    elif T==1:
        print("Case %d: There is one tree." %(i+1))
    else:
        print("Case %d: No trees." %(i+1))
#print(f'Case {T}: A forest of {cnt} trees.')
#print("Case {}: A forest of {} trees.".format(time, cnt))
#위 두방법이 더 편할듯