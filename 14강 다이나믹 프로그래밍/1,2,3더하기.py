
d= [0,1,2,4]
for i in range(4,11):
    d.append(d[i-1] + d[i-2] + d[i-3]) #미리다 구해놓는게 효율적
for i in range(int(input())):
    print(d[int(input())])