import sys
input = sys.stdin.readline

x = input().rstrip()
y = input().rstrip()
xlen = len(x)
ylen = len(y)
# LCS = [[0]*(len(x)+1)]*(len(y)+1)
LCS = [[0 for _ in range(ylen+1)] for _ in range(xlen+1)]

for i in range(1,xlen+1):
    for j in range(1,ylen+1):
        if x[i-1] == y[j-1]:
            LCS[i][j] = LCS[i-1][j-1] +1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
print(LCS[-1][-1])