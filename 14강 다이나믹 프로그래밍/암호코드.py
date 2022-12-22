import sys
arr = sys.stdin.readline().rstrip()
n = len(arr)
dp = [[0 for _ in range(2)] for _ in range(n+1)]
dp[1][0] = 0
dp[1][1] = 1

if arr[0] == "0":
    print(0)
    exit()
for i in range(2,n+1):
    dp[i][0] = dp[i-1][1]%1000000
    dp[i][1] = (dp[i-1][0]+dp[i-1][1])%1000000
    if int(arr[i-1])==0:
        if 0<int(arr[i-2])<=2:
           dp[i][1]=0
        else:
            print(0)
            exit()
    elif int(arr[i-2] + arr[i-1]) > 26:
        dp[i][0]=0
print((dp[n][0]+dp[n][1])%1000000)


s = input()
sl = len(s)
mod = 1000000
d = [0] * 5001

d[0] = 1
for i in range(sl):
    j = i + 1
    n = int(s[i])
    m = int(s[i-1] + s[i])
    if n > 0 and n < 10:
        d[j] += d[j-1]
        d[j] %= mod
    if m >= 10 and m <= 26:
        d[j] += d[j-2]
        d[j] %= mod
print(d[sl])