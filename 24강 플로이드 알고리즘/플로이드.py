#플로이드 알고리즘은 O(N^3)의 시간복잡도를 가져서 10^2의 정점을 가지는 본 예제의 경우 10^6의 시간복잡도 
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [[sys.maxsize]*n for _ in range(n)]
for _ in range(m):
    a,b,cost = map(int,input().split())
    if cost<arr[a-1][b-1]: arr[a-1][b-1] =cost #두 도시 지나는 버스가 여러개있음

for mid in range(n):    # mid는 반드시 제일 바깥쪽 for에 넣어야됨
    for st in range(n):
        for en in range(n):
            if st==en: arr[st][en] = 0  #자기자신으로 가는경우 0
            # arr[st][en] = min(arr[st][en],arr[st][mid]+arr[mid][en])
            if arr[st][en] > arr[st][mid]+arr[mid][en]:  #비교가 대입보다 빠른점을 이용해 매번대입하는 상황에서 시간을 줄일수있음, 상수시간 최적화
                arr[st][en] = arr[st][mid]+arr[mid][en]

for st in range(n):
    for en in range(n):
        print(arr[st][en] if arr[st][en]!= sys.maxsize else 0,end=" ")
    print()