# 자식갯수 > 직속자식만이이니까 bfs 하는 도중에 별도 리스트에 추가 
#
import sys
from collections import deque

input= sys.stdin.readline

n = int(input())
name = input().split()
m = int(input())

adj = {i:[] for i in name}
for _ in range(m):
    