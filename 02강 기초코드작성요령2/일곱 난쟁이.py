
data = []
for i in range(9):
    data.append(int(input()))



def func(data):
    for i in data:
        tmp = data.copy()
        tmp.remove(i)
        for j in tmp:
            tmp2 = tmp.copy()
            tmp2.remove(j)
            if sum(tmp2) == 100:
                return tmp2
                # print(*sorted(tmp2), sep="\n")
                # print(tmp2)

print(*sorted(func(data)), sep="\n")