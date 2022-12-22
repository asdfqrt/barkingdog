import sys
N = int(input())
list = []

for _ in range(N):
    cmd = sys.stdin.readline().rstrip()
    if cmd == "pop":
        try:
            print(list.pop(0))
        except:
            print(-1)
    elif cmd == "size":
        print(len(list))
    elif cmd == "empty":
        if list:
            print(0)
        else:
            print(1)
    elif cmd == "front":
        try:
            print(list[0])
        except:
            print(-1)
    elif cmd == "back":
        try:
            print(list[-1])
        except:
            print(-1)
    else:
        list.append(cmd[5:])

