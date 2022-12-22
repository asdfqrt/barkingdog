N = []
for i in range(9):
    N.append(int(input()))
max = max(N)
print(max)
print(N.index(max)+1)