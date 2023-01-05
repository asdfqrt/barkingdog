import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())
pblist = []
max_pblist = []
exist = {}
for _ in range(n):
    num,lev = map(int,input().split())
    heappush(pblist,[lev,num])  #첫번째 항목 lev가 같으면 그이후 항목 num이 작은 순으로 정렬됨
    heappush(max_pblist,[-lev,-num])    #첫번째 항목 -lev가 같으면 그 이후 항목 -num이 작은 순서대로 정렬되네
    exist[num] = True
m = int(input())


for _ in range(m):
    ord = input().split()

    if ord[0] == "recommend":
        if ord[1] == "-1": print(pblist[0][1])
        else: print(-max_pblist[0][1])

    elif ord[0] == "add":
        exist[int(ord[1])] = True
        heappush(pblist,[int(ord[2]),int(ord[1])])
        heappush(max_pblist,[-int(ord[2]),-int(ord[1])])

    elif ord[0] == "solved":
        exist[int(ord[1])] = False
        while not exist[pblist[0][1]]: heappop(pblist)
        while not exist[-max_pblist[0][1]]: heappop(max_pblist)





        # temp = {}
        # a = heappop(pblist)
        # while a[1] != int(ord[1]):
        #     temp[a[1]] = a[0]
        #     a = heappop(pblist)
        # for i in temp:
        #     heappush(pblist,[temp[i],i])

        # temp = {}
        # a = heappop(max_pblist)
        # while a[1] != int(ord[1]):
        #     temp[a[1]] = a[0]
        #     a = heappop(max_pblist)
        # for i in temp:
        #     heappush(max_pblist,[temp[i],i])
        
        
        
        # temp = []
        # temp.append(heappop(pblist))
        # while temp[-1][1] != int(ord[1]):
        #     temp.append(heappop(pblist))
        # pblist = list(merge(pblist,temp[:-1]))


        # temp = []
        # temp.append(heappop(max_pblist))
        # while temp[-1][1] != int(ord[1]):
        #     temp.append(heappop(max_pblist))
        # max_pblist = list(merge(max_pblist,temp[:-1]))



