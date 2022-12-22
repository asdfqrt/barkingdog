#D를 i번째 계단까지 올라섰을때 밟을 계단의 합의 최대값으로 할때
# n= int(input())
# arr =[0]
# for i in range(n):
#     arr.append(int(input()))
# if n==1:
#     print(arr[1])
#     exit()
# d = [[0,0,0],[0,arr[1],0],[0,arr[2],arr[1]+arr[2]]]
# for i in range(3,n+1):
#     d.append([0,
#     max(d[i-2][1],d[i-2][2])+arr[i],
#     d[i-1][1]+arr[i]])
# print(max(d[n][1],d[n][2])) 

#D를 i번째 계단까지 올라섰을때 밟지않을 계단의 합의 최솟값으로 할때,i번째는 밟지않는 계단
n= int(input())
arr =[0]
for i in range(n):
    arr.append(int(input()))
if n<3:
    print(sum(arr))
    exit()
d = [0,arr[1],arr[2],arr[3]]
for i in range(4,n):
    d.append(min(d[i-2],d[i-3])+arr[i])
print(sum(arr)-min(d[n-2],d[n-1]))