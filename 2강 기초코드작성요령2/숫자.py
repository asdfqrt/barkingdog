data = sorted(list(map(int,input().split())))
if data[0] == data[1]:
    print("0")
else:
    print(data[1]-data[0]-1)
    print(*range(data[0]+1,data[1]))