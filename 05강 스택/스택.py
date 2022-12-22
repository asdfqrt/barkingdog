import sys
N = int(input())
list = []

for _ in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push":
        list.append(cmd[1])
    elif cmd[0] == "pop":
        if list:
            print(list.pop())
        else:
            print("-1")
    elif cmd[0] == "size":
        print(len(list))
    elif cmd[0] == "empty":
        if list:
            print("0")
        else:
            print("1")
    else:
        if list:
            print(*list[-1],sep="")
        else:
            print("-1")