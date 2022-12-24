import sys
import bisect
input = sys.stdin.readline

n = int(input())
arr= list(map(int,input().split()))
d = [arr[0]]  #가장 긴 증가하는 부분수열이 아니라 가장 긴 증가하는 부분수열과 같은 길이를 가지는 수열

for i in range(1,n):
    if d[-1] < arr[i]:
        d.append(arr[i])
    else:
        d[bisect.bisect_left(d,arr[i])] = arr[i]

print(len(d))
    
#실제로는 LIS를 만족하지 않는 상태
#d의 기존 값을 더 작은 값으로 대치하여 이후 원소가 더 많이 들어 올 수 있는 가능성을 넓히는 과정
#어디까지나 '길이'를 구하는데 한정하여 이분탐색을 활용해 풀이 할 수 있다
