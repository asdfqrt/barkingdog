import sys


n = int(input())
answer = []

for i in range(n):
    befcur = []
    aftcur = []

    x = sys.stdin.readline().rstrip()
    for i in range(len(x)):
        if x[i] == "<":
                if befcur:
                    aftcur.append(befcur.pop())
        elif x[i] == ">":
            if aftcur:
                befcur.append(aftcur.pop())
        elif x[i] == "-":
            if befcur:
                befcur.pop()
        else:
            befcur.append(x[i])
    
    answer.append("".join(befcur + aftcur[::-1]))
print(*answer,sep="\n")