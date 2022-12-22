t= int(input())
up = [1,1,2,4]
down = [1,2,3,5]


for i in range(4,100):
    up.append(down[i-1]+down[i-3])
    down.append(up[i]+up[i-2])


for _ in range(t):
    n= int(input())
    if n%2 ==0:
        print(down[(n//2)-1])
    else:
        print(up[(n-1)//2])