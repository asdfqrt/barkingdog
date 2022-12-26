#수의 갯수자체는 1만개이지만 합이 300억제한, 어짜피 근데 큰수 연산해도 시간제한이랑 관련없을거 같긴함

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int,input().split()))

st=0
en=0
localsum=arr[0]
cnt = 0

while st<=en<n:
    if localsum==m: #배열이 자연수이기 때문에 localsum이 m도달했을때 en만 늘리면 무조건 m넘어감< 배제해도된다
        cnt += 1

        st +=1
        en +=1
        if st<=en<n : localsum += arr[en] - arr[st-1]
        
    elif localsum<m:
        en +=1
        if en<n : localsum += arr[en]
    else:   #st=en일때 단일 숫자가 m을 넘어가는경우 st만 이동시키면 while문 끝나므로 단일 숫자인지 아닌지 확인> 단일아니면 st만 이동,단일이면 st,en 둘다이동
        if st<en<n:
            localsum -= arr[st]
            st+=1
        elif st==en<n:
            st+=1
            en+=1
            if st<=en<n : localsum += arr[en] - arr[st-1]




print(cnt)



################################
import sys

n, m = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
k = 0
tmp = 0
for i in a:
    tmp += i
    while tmp > m:
        tmp -= a[k]
        k += 1
    cnt += (tmp == m)
print(cnt)
##################################



N, M = map(int, input().split(' '))
A = list(map(int, input().split(' ')))
cnt = 0
x = 0
end = 0

for start in range(N) :     #이게 좋은듯? 어짜피 st는 무조건 한칸씩 처음부터 끝까지 이동시키니까 for로 한칸씩 이동시키도록 하면 코드 많이 단축됨
    while x < M and end < N :
        x += A[end]
        end += 1
    if x == M :
        cnt += 1
    x -= A[start]

print(cnt)

##################################