import sys
from collections import deque
input= sys.stdin.readline
t= int(input())

for _ in range(t):
    rotate = False
    p = input().rstrip()
    n = int(input())
    arr = input().rstrip().strip('[]').split(',')
    if arr==['']: arr=[]
    q = deque(arr)
    
    try:    
        for order in p:    
            if order =="R":
                rotate = not rotate
            else:
                if not rotate:
                    q.popleft()
                else:
                    q.pop()

        if rotate: q.reverse()
        print( "[" + ",".join(q) + "]" )
    except:
        print("error")
    
