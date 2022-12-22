import sys

# def solution(N,X):
#     answer = []


#     return answer


data = list(map(int, input().split()))
N = data[0]
X = data[1]

data = list(map(int, input().split()))
for i in range(len(data)):
    if data[i] >= X:
        data[i] = 0
while 0 in data:
    data.remove(0)
print(*data)

# print(solution(a,b,c))
