import math

N = int(input())
time = list(map(int,input().split()))
mprice = 0
yprice = 0
for i in range(N):
    yprice += (math.floor(time[i] / 30)+1) * 10
    mprice += (math.floor(time[i] / 60)+1) * 15


if mprice < yprice:
    print("M", mprice)
elif mprice == yprice:
    print("Y M", mprice)
else:
    print("Y", yprice)
