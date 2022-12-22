# import math
# data = int(input())


# numlist = [0] * 10
# for x in str(data):
#     if x == "6" or x == "9":
#         numlist[6] += 1
#         numlist[9] += 1
#     else:
#         numlist[int(x)] += 1

# numlist[6] = math.ceil(numlist[6]/2)
# numlist[9] = math.ceil(numlist[9]/2)
# print(max(numlist))



a=[0]*10
for i in input():a[int(i)]+=1
a[6]=(a[6]+a[-1]+1)//2
print(max(a[:-1]))