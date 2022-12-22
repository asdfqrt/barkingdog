data = list(map(int,input().split()))
data = sorted(data)
if data[0] == data[1]:
    if data[1] == data[2]:
        answer = 10000 + data[0] * 1000
    else:
        answer = 1000 + data[0] * 100
elif data[1] == data[2]:
    answer = 1000+ data[1] * 100
else:
    answer = max(data) *100

print(answer)
