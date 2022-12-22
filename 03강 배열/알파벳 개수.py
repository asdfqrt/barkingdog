# from string import ascii_lowercase
# alphabet = list(ascii_lowercase)
# numlist = [0 for i in range(len(alphabet))]
# data = input()

# for i in range(len(alphabet)):
#     numlist[i] = data.count(alphabet[i])
# print(*numlist)



apb = [0]*26
for x in input():
    apb[ord(x)-97] += 1
print(*apb)



