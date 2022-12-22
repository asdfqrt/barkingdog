input()
a = map(int,input().split())
b = set(map(int,input().split()))
cnt = 0
result = []

for i in a:
    if i not in b:
        cnt += 1
        result.append(i)
result.sort()
print(cnt)
print(*result)