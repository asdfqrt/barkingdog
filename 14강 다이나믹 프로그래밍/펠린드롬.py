import sys
input =sys.stdin.readline

n = int(input())
arr = [0] + list(map(int,input().split()))
m = int(input())
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for k in range(1,n+1):    #k칸 짜리 팰린드롭 확인
    for i in range(1,n-k+2):
        if k==1:
            dp[i][i]=1
        elif k==2 or k==3:
            if arr[i]==arr[i+k-1]: dp[i][i+k-1]=1
        elif dp[i+1][i+k-2]==1 and arr[i]==arr[i+k-1]: dp[i][i+k-1]=1


for _ in range(m):
    start,end = map(int,input().split())
    print(dp[start][end])
