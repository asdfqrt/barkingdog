n = int(input())
d= [[0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1]]    #d[i][k] = 제일 앞자리가 k인 i자리 계단수의 갯수

for i in range(2,n+1):
    d.append([d[i-1][1]% 1000000000])
    for k in range(1,9):
        d[i].append((d[i-1][k-1] + d[i-1][k+1])% 1000000000)
    d[i].append(d[i-1][8]%1000000000)
print(sum(d[n][1:])%1000000000)