import sys, heapq
from collections import defaultdict
input= sys.stdin.readline

t= int(input())
for _ in range(t):
    k=int(input())
    heap = []
    max_heap = []
    # dic = {}
    dic = defaultdict(int) # 이렇게 하면 값을 지정하지 않은 키의 초기값이 0이됨

    for _ in range(k):
        ord, num = input().split()
        num = int(num)
        if ord == "I":
            # if num in dic: dic[num] += 1
            # else: dic[num] = 1
            dic[num]+=1  #defaultdic을 사용햇기에 안에 있는지 확인하는 조건문이 필요없어짐 
            heapq.heappush(heap,num)
            heapq.heappush(max_heap,-num)
        elif num == -1:
            while heap:
                minnum = heapq.heappop(heap)
                if dic[minnum] !=0: #원래부터 dic에 갯수가 0이었다 > 이미 지워졋어야했는데 안지워지고 남아있던 찌꺼기이기에 지우고 한번더
                    dic[minnum] -= 1
                    break
        else:
            while max_heap:
                maxnum = -heapq.heappop(max_heap)
                if dic[maxnum] !=0:
                    dic[maxnum] -= 1
                    break                  
    while heap and dic[heap[0]] == 0: heapq.heappop(heap)   #힙의 첫 값이 dic에서 0이라 없어야되는데 있는경우는 싹다 지움
    while max_heap and dic[-max_heap[0]] == 0: heapq.heappop(max_heap)

    if heap: print(-max_heap[0], heap[0])
    else: print("EMPTY")

