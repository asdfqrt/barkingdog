# 이분 그래프의 조건은 아마 간선 1개짜리 사이클이 없으면 되는거 같음 > 아님 123 456이면 상관x
# 아니라 한개의 간선을 넘을때 마다 다른 집합으로 넘어가야됨 >> 3색정리처럼 2색으로 표현해야됨
# vis를 true false 대신 False, red, green으로 하면 될듯?
# dfs로 탐색하되 처음 시작한 노드의 집단에서 떨어져 있을수도 있으니 for로 전체 노드를 다 시작 지점으로 한번씩 체크해야될듯
# 집단 자체가 떨어져 있는 경우 그 집단내에서만 구별되도 되니까 굳이 다 확인할 필요는 없음
# 제한시간 2초 TLE 뜸 >> 모든 시작점 확인 xx 이미 확인된 정점이면 더 확인하지 말고 넘어가야될듯 >> 시작지점 저장 > set에 모든정점 다넣어놓고 확인할때마다 제외
# 시간 더 줄이는 방법? red blue 를 문자 아닌 True False나 숫자로 바꾸면 될듯? >> 안되네
# startpoint를 없애고 vis를 시작점 돌리는 for문밖에서 선언해 유지시키면 set의 pop도 필요없고 False인 부분만 확인하면 되서 더 빠를듯

def dfs(cur,color):
    vis[cur] = color
    # startpoint.discard(cur)    #remove 쓰면 startpoint.pop으로 시작지점목록에서 삭제된 첫 정점에서 에러
    # countercolor = "red" if color == "blue" else "blue"
    countercolor = red if color == blue else blue
    for dir in adj[cur]:
        if not vis[dir] and not dfs(dir,countercolor): return False # 빈 곳이라 방문 했는데 하위에서 False띄우면 false 반환해야됨
        elif vis[dir] == color: return False    # 똑같은 색 칠해져 있을경우
                                                # 제대로 반대색 색칠되어 있을경우
    return True #다돌았는데 문제없으면 True 반환
import sys
input= sys.stdin.readline
sys.setrecursionlimit(10**6)
red, blue = 1, -1
k = int(input())
for _ in range(k):
    v,e = map(int,input().split())
    adj = [[] for _ in range(v+1)]  #굳이 0 안넣더라도 빈 2차원 배열 만들수 있음 >> 0방문하는 시간절약
    # startpoint = set(i+1 for i in range(v))
    ans = True
    for _ in range(e):
        a,b = map(int,input().split())
        adj[a].append(b)
        adj[b].append(a)

    # # for st in range(1,v+1):
    # while startpoint:
    #     st = startpoint.pop()
    #     vis = [True] + [False]*v
    #     # if not dfs(st,"red"):
    #     if not dfs(st,red):
    #         ans = False
    #         break
    vis = [True] + [False]*v
    for st in range(1,v+1):
        if not vis[st] and not dfs(st,red):
            ans=False
            break


    print("YES" if ans else "NO")




