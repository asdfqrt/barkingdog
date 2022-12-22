data= [0,0,0]

for i in range(len(data)):
    data[i] = list(map(int,input().split()))

for i in data:
    if sum(i) == 4:
        answer = "E"
    elif sum(i) == 3:
        answer = "A"
    elif sum(i) == 2:
        answer = "B"
    elif sum(i) == 1:
        answer = "C"
    else:
        answer = "D"
        
    print(answer)