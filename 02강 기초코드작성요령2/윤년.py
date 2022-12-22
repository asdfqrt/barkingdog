data = int(input())
answer = 0

if data%100 != 0:
    if data%4 == 0:
        answer = 1
elif data%400 == 0:
    answer = 1

print(answer)
