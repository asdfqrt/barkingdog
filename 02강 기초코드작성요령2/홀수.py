
data = []

for i in range(7):
    num = int(input())
    if num % 2 != 0: 
        data.append(num)
        
if data == []:
    print("-1")
else:
    print(sum(data))
    print(sorted(data)[0])
