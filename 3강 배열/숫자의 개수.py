num1 = int(input())
num2 = int(input())
num3 = int(input())
res = num1 * num2 * num3 
numlist = [0] * 10

for x in str(res):
    numlist[int(x)] += 1

print(*numlist, sep="\n") 

