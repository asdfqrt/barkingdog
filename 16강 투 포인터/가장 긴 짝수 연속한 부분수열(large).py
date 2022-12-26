import sys
input = sys.stdin.readline

n,k = map(int,input().split())

def jjak(n):
    if int(n)%2==0:
        return True
    return False

arr = list(map(jjak,input().split()))

en=0
fnum = 0 if arr[0] else 1
ans = 0

for st in range(n):
    while en<n-1:
        if arr[en+1]:   #en의 다음이 짝수일 경우 en증가시킴
            en +=1
        elif fnum != k: #en다음이 홀수이지만 봐주기 k회가 남아있으면 증가시키고 한번더 봐줬다고 기록
            fnum +=1
            en +=1
        else:
            break   #en의 다음이 홀수이고 봐주기도 다썼다면 거기까지 길이 기록
    ans = max(ans,en-st+1-fnum)
    if not arr[st] and fnum > 0:    #st증가전에 st해당부분이 홀수였으면 봐주기사용 1회 경감
        fnum -= 1
print(ans)


