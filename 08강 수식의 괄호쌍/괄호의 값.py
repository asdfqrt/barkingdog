import sys
from collections import deque

x = sys.stdin.readline().rstrip()
list = deque([])
cal = False
cnt = 1
ans = 0

for i in x:
    if i == "(":
        cnt *= 2
        list.append(i)
        cal = True
    elif i == "[":
        cnt *= 3
        list.append(i)
        cal = True
    elif i == ")":
        try:
            if list.pop() != "(":
                ans = 0
                break
            elif cal:
                ans += cnt
                cnt /= 2
                cal = False
            else:
                cnt /= 2
        except:
            ans = 0
            break
    else:
        try:
            if list.pop() != "[":
                ans = 0
                break
            elif cal:
                ans += cnt
                cnt /= 3
                cal = False
            else:
                cnt /= 3
        except:
            ans = 0
            break
if int(cnt) == 1:
    print(int(ans))
else:
    print(0)


