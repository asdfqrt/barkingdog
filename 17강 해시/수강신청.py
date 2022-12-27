#1초제한에 N=10^5이니까 O(N)이면될듯

import sys
input = sys.stdin.readline

k,l = map(int,input().split())
arr = {}
for i in range(l):
    stunum = input().rstrip()
    arr[stunum] = i

###############################
# ord = [sys.maxsize]*500001
# for i in arr:
#     ord[arr[i]] = i

# for i in range(l):
#     if ord[i] != sys.maxsize:
#         print(ord[i])
#         k -= 1
#         if k==0: break
###############################
# for i in sorted(arr.items(), key=lambda x: x[1])[:k]:   #arr.items()하면 ('20103324',0)식으로 안에 값까지 뜨고 sorted( key=lamda x: x[1])하면 두번째에 나오는 안에 값 기준으로 정렬할 수있음
#     print(i[0])
###############################
print(*sorted(arr, key=lambda x:arr[x])[:k], sep="\n") #이렇게하면 '20103324'만 뜨면서 sort는 arr[20103324]의 값인 0을 기준으로 됨