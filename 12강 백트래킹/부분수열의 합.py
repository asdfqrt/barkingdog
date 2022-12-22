n,s = map(int, input().split())
cnt = 0
arr = list(map(int,input().split()))

def func(cur, tot):
    if cur==n:  #마지막 요소를 확인하고 있을경우
        if tot==s:  #만약 현재까지의 부분집함의 합이 주어진 조건 s과 같다면
            global cnt
            cnt += 1
        return
    func(cur+1, tot) #cur번째 수가 안 들어가는경우, cur+1번째수 들어갈지말지 판단, tot는 그대로
    func(cur+1, tot+arr[cur]) #cur번째수가 들어가는경우 , cur+1번째수 들어갈지 말지 판다, tot에 cur번째 요소 추가


func(0,0)
if s==0:
    cnt -= 1
print(cnt)


