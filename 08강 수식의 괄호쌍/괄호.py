import sys
from collections import deque


T = int(input())
for _ in range(T):
    x = sys.stdin.readline().rstrip()
    list = deque([])
    answer = "NO"

    for i in x:
        if i == ")":
            try:
                if list[-1] == "(":
                    list.pop()
            except:
                list.append(i)
                break
        else:
            list.append(i)



    if len(list) == 0:
        answer = "YES"
    print(answer)


# for _ in range(int(input())):
#   st = input()
#   while(1):
#     if '()' in st:
#       st = st.replace('()','')
#     else:
#       break
#   if st =='':
#     print('YES')
#   else:
#     print("NO")

