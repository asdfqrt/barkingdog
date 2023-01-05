# 구역의 개수가 10^5 인걸 보니 쿼리 갯수 10^5 마다 매 구역값 바꾸면 10^10개 연산 해야되므로 아닌듯(remove불가)
# 2 x 에서 10^9 만큼이동하니 %로 나눠서 해야 해야할듯
# 제일 가까운 명소는 heap중 지나온거 다 뺀거
# 명소의 지정을 푸는건 exist = {}로 만들어서 없어질때까지 while 문으로 처리해야할듯

# import sys
# from heapq import heappop, heappush
# from collections import defaultdict

# input= sys.stdin.readline
# n,q = map(int,input().split())
# hotplace = []
# temp = []
# exist = defaultdict(bool)

# for where,i in enumerate(map(int,input().split())):
#     if i == 1:
#         exist[where+1] = True
#         heappush(hotplace,where+1)
# x = 1


# for _ in range(q):
#     query = input().split()

#     if query[0] == "1":
#         exist[int(int(query[1]))] = not exist[int(int(query[1]))] #True False반대로
#         if exist[int(int(query[1]))]: heappush(hotplace,int(int(query[1])))   #추가하는 경우는 바로 추가, 지우는건 나중에 한번에

#     elif query[0] == "2":
#         x = x+int(int(query[1]))
#         if x > n:   #한바퀴 돌고나면 temp에 있던거 다시 전부 hotplace에 넣기
#             while temp: heappush(hotplace,heappop(temp))
#             x %= n
#             if x == 0: x = n

#     else:
#         #x언더의 hotplace들 싹다 지워야됨
#         while temp:
#             if not exist[temp[0]]: heappop(temp)
#             elif temp[0] > x: heappush(hotplace,heappop(temp))
#             else: break
            
#         while hotplace:
#             if not exist[hotplace[0]]: heappop(hotplace)
#             elif hotplace[0] < x: heappush(temp,heappop(hotplace))
#             else: break

#         if hotplace: print(hotplace[0]-x)
#         elif temp: print(n-x+temp[0])
#         else: print(-1)

###############################################

# import sys, bisect
# from heapq import heappop, heappush

# input= sys.stdin.readline
# n,q = map(int,input().split())
# hotplace = []
# temp = []
# exist = set()
# for where,i in enumerate(map(int,input().split())):
#     if i == 1:
#         exist.add(where+1)
#         heappush(hotplace,where+1)
# x = 1
# for _ in range(q):
#     query = input().split()

#     if query[0] == "1":
#         if int(query[1]) in exist:
#             exist.remove(int(query[1]))
#             while hotplace[0] != int(query[1]): temp.append(heappop(hotplace))
#             heappop(hotplace)
#             while temp: heappush(hotplace,temp.pop())    #이 방법도 결국 비효율 적이지 않나? cpp처럼 바로 erase가능한거 아니면 삭제 NlogN + 복구 NlogN걸리는데

#         else:
#             exist.add(int(query[1]))
#             heappush(hotplace,int(query[1]))
        
#     elif query[0] == "2":
#         x=(x+int(query[1])-1)%n + 1 

#     else:
#         idx = bisect.bisect_left(hotplace,x)    # 애초에 heapq에서 bisect가 먹지도 않을텐데
#         if idx == len(hotplace):
#             if hotplace: print(n-x+hotplace[0])
#             else: print(-1)
#         else: print(hotplace[idx]-x)

###############################################

# import sys
# from collections import defaultdict

# input = sys.stdin.readline
# MIS = lambda: map(int, input().split())
# MAXINT = int(1e06)
# cur = 1

# def one(s, e, i):
#   if i < s or i > e:
#     return tree[(s, e)]
#   if s == e:
#     if L[i]: tree[(s, e)] = i
#     else: tree[(s, e)] = MAXINT
#     return tree[(s, e)]
#   mid = (s + e) // 2
#   tree[(s, e)] = min(one(s, mid, i), one(mid + 1, e, i))
#   return tree[(s, e)]

# def two(x):
#   global cur, N
#   cur = (cur + x) % N
#   if cur == 0: cur = N
  
# def three(s, e):
#   global cur, N
#   if s > N or e < cur: return MAXINT
#   if cur <= s and e <= N: return tree[(s, e)]
#   mid = (s + e) // 2
#   return min(three(s, mid), three(mid + 1, e))

# N, Q = MIS()
# L = [0] + list(MIS())
# tree = defaultdict(lambda: MAXINT)
# cur = 1

# for i in range(1, N+1):
#   if L[i]: one(1, N, i)

# for _ in range(Q):
#   line = list(MIS())
#   if line[0] == 1:
#     L[line[1]] ^= 1
#     one(1, N, line[1])
#   elif line[0] == 2:
#     two(line[1])
#   elif line[0] == 3:
#     ans = three(1, N)
#     if ans != MAXINT:
#       print(ans - cur)
#       continue
#     if tree[(1, N)] != MAXINT:
#       print(N - cur + tree[(1, N)])
#       continue
#     print(-1)

##################################################
import sys

rr = sys.stdin.readline
MM = 987654321

def update(node, l, r, target):
    if target < l or target > r: return seg[node]
    if l == r:
        if L[target]: seg[node] = target
        else:seg[node] = MM
        return seg[node]

    mid = (l+r)//2
    seg[node] = min(update(node*2, l, mid, target), update(node*2+1, mid+1, r, target))
    return seg[node]

def query(node, l, r, wl, wr):
    if (l > wr or r < wl): return MM
    if (wl <= l and r <= wr): return seg[node]
    mid = (l+r)//2
    return min(query(node*2, l, mid, wl, wr), query(node*2+1, mid+1, r, wl, wr))


N, Q = map(int, rr().split())
L = [0] + list(map(int, rr().split()))
seg = [MM]*(4*N)

for i in range(1, N+1):
    if L[i]: update(1, 1, N, i)

now = 1

for _ in range(Q):
    cmd = list(map(int, rr().split()))
    if cmd[0] == 1:
        L[cmd[1]]^=1
        update(1, 1, N, cmd[1])
    elif cmd[0] == 2:
        now = (now+cmd[1])%N
        if now == 0: now = N
    elif cmd[0] == 3:
        a = query(1, 1, N, now, N)
        if a != MM:
            print(a-now)
            continue
        a = query(1, 1, N, 1, now)
        if a != MM:
            print(a-now+N)
            continue
        print(-1)