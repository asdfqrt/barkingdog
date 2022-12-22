t = int(input())

arr0 = [1,0]
arr1 = [0,1]

for i in range(2,41):
    arr0.append(arr0[i-1]+arr0[i-2])
    arr1.append(arr1[i-1]+arr1[i-2])

for _ in range(t):
    num = int(input())
    print(arr0[num],arr1[num])