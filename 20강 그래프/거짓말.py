# 진실을 알고있는 사람 >> 전염병환자임. 얘 근처에 닿으면 다 전염병걸림
# 전염병이 없는 파티를 고르는 문제임
# 그래프로 진실을 알고있는 사람과 모여져 있는 사람 다 set에 넣어
# 입력받은 순서 그대로 파티도 저장해둬야 될듯

import sys

input= sys.stdin.readline
n,m = map(int,input().split())

adj = [[False]*n for _ in range(n)]

plague = list(map(int,input().split()))
plaset = set()
for i in range(1,plague[0]+1):
    plaset.add(plague[i])


adj = [[False]*n for _ in range(n)]
people = []
for k in range(m):
    people.append(list(map(int,input().split())))
    for i in range(1,people[k][0]):
        for j in range(i+1,people[k][0]+1):
            adj[people[k][i]-1][people[k][j]-1] = True
            adj[people[k][j]-1][people[k][i]-1] = True

vis = [False] *n

def dfs(cur):
    vis[cur] = True
    for dir, open in enumerate(adj[cur]):
        if open and not vis[dir]:
            plaset.add(dir+1)
            dfs(dir)

for i in range(plague[0]):
    dfs(plague[i+1]-1)
ans = 0
for i in range(m):
    infect = False
    for j in people[i][1:]: #파티에 감염된사람 아무도 없으면 ans+1
        if j in plaset:
            infect = True
            break
    ans +=1 if not infect else 0
print(ans)


######################
# dfs나 트리 구조를 쓰지 않고도 set 자료형의 합집합, 교집합 사용해 감염자가 party안에 있으면 그파티를 통채로 감염자리스트에 넣으면 좋은듯
import sys

input= sys.stdin.readline
n,m = map(int,input().split())

plague = set(input().split()[1:])
party = []

for _ in range(m):
    party.append(set(input().split()[1:]))

for _ in range(m): # party가 (1,2) (3,4), ...., (99,100) 식으로 주어지고 plauge를 100주면 1까지 오는데 최대 97번 반복해야됨
    for people in party:
        if people & plague: plague = plague.union(people)    # for문 써서 people 다 펼칠필요 없이 & 쓰면 교집합 나옴, union이 합집합,
            #plague.union으로 바로 합해지는게 아님 plague = plague.union ~~ 해줘야됨
        

ans = 0
for people in party:
    if people & plague == set(): ans+=1   #교집합없는 공집합일시
print(ans)