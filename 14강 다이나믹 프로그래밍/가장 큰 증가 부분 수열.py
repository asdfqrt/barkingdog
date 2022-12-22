n = int(input())
arr = list(map(int,input().split()))
d = arr[:]
for i in range(1,n):
    for j in range(i):
        if arr[i] > arr[j] and d[i]<d[j]+arr[i]:
            d[i] = d[j] + arr[i]

print(max(d))


# n = int(input())
# arr = list(map(int,input().split()))
# d = [arr[0]]
# for i in range(1,n):
#     if arr[i] > arr[i-1]:
#         d.append(d[i-1]+arr[i])
#     else:
#         pos = i-1
#         while pos!=-1 and arr[pos] >= arr[i]:
#             pos -= 1
#         if pos == -1:
#             d.append(arr[i])
#         else:
#             d.append(d[pos]+arr[i])
# print(max(d))


