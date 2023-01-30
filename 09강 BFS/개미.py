import sys
input =sys.stdin.readline
w,h = map(int,input().split())
x,y = map(int,input().split())
t = int(input())

x += t
y += t
x %= (2*w)
y %= (2*h)

if x >= w:
    x = w - (x-w)
if y >= h:
    y = h - (y-h)
print(x,y)