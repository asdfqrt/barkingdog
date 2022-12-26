#시간 제한 1초, N = 3*10^4이니까 O(N^2)까지는 괜찮을듯

# import sys
# input= sys.stdin.readline

# n,d,k,c = map(int,input().split())
# arr= []
# for _ in range(n):
#     arr.append(int(input()))   #문제에서 k<N이라한거보니까 한바퀴도 안돔 걍 두배하면됨
# arr = arr*2



# en=0
# ateplate = 0    #중복을 포합한 여태 먹은 접시 갯수
# uniqplate = 0   #중복을 제외한 여태 먹은 접시 갯수
# cused = False
# isused = [0]*d  #여태 먹은 초밥 종류
# ans=0


# for st in range(n):
#     while en<(2*n)-1:
#         if arr[en] == c and not cused:    #쿠폰쓰면 공짜로 한개 추가
#             isused[arr[en]-1] += 1
#             uniqplate +=1
#             en +=1
#             cused = True
#             ateplate +=1

#         elif ateplate <= k:  #쿠폰안쓰면 plate갯수가 연속접시갯수k보다 작을때만 한개 추가
#             if isused[arr[en]-1] == 0:
#                 uniqplate +=1
#             isused[arr[en]-1] += 1
#             en +=1
#             ateplate +=1
#         else:   #쿠폰용 접시도 아니고 연속접시갯수보다 넘게 먹었으면 그만먹어
#             break
#     ans = max(uniqplate if cused else uniqplate+1,ans) #쿠폰초밥 못먹었으면 하나 더 줌 
#     # if en==11:
#     #     print("a")
#     isused[arr[st]-1] -= 1
#     ateplate -= 1
#     if isused[arr[st]-1] == 0:
#         uniqplate -=1
#     if arr[st] == c and isused[arr[st]-1] ==0:    #첫번쨰꺼가 유일하게 쿠폰쓴거였으면 쿠폰 안썻다고 표기 다른 쿠폰초밥이 더 있었으면 쿠폰은 쓴 그대로 두고 ateplate한개 낮추기X 아펭서 이미낮춤
#         cused = False

# print(ans)
    

####################
#문제 조건을 잘못 이해한듯
#k개를 무조건 연속해서 먹고나서 or 먹기전에 쿠폰 초밥을 먹어야되나봄


# import sys
# input= sys.stdin.readline

# n,d,k,c = map(int,input().split())
# arr= []
# for _ in range(n):
#     arr.append(int(input()))   #문제에서 k<N이라한거보니까 한바퀴도 안돔 걍 두배하면됨
# arr = arr*2
# isused = [0]*d

# ans = 0
# en = 0
# cnt = 0
# uniq = 0
# cused = False

# for st in range(n):
#     if arr[st]==c:
#         cnt -= 1
#         cused = True
#     while True:
#         if cnt<k:
#             isused[arr[en]-1] +=1
#             if isused[arr[en]-1] == 1:
#                 uniq += 1
#             en+=1
#             cnt+=1
#         elif arr[en] == c and cused==False:
#             isused[arr[en]-1] +=1
#             if isused[arr[en]-1] == 1:
#                 uniq += 1
#         else:
#             break
#     ans = max(ans,uniq)
#     if arr[st] != c:
#         cnt-=1
#         isused[arr[st]-1] -=1
#     else:
#         cused=False
# print(ans)
    

# #이렇게 푸는거 아닌듯 조건이 너무너무 복잡해짐






import sys
input= sys.stdin.readline


def eat(sushi):
    global ateKindCount
    global answer
    if (ateCount[sushi] == 0):
        ateKindCount += 1
        answer = max(answer, ateKindCount)
    ateCount[sushi] += 1

def overeat(sushi):
    global ateKindCount
    ateCount[sushi] -= 1
    if ateCount[sushi] ==0: ateKindCount -= 1


dishesCount,sushiKindCount,chainingEatCount,couponNum = map(int,input().split())
dishes= []
ateCount = [0]*(sushiKindCount+1)
ateCount[couponNum] += 1
ateKindCount =1
answer = 1


for i in range(dishesCount):
    dishes.append(int(input()))

dishes = dishes * 2

for i in range(dishesCount*2):
    if i>= chainingEatCount: overeat(dishes[i-chainingEatCount])
    eat(dishes[i])

print(answer)




