# import bisect
# import sys

# input = sys.stdin.readline
# n = int(input())
# arr = list(map(int,input().split()))
# arr.sort()
# cnt = 0

# for i in range(n-1):
#     for j in range(i+1,n):
#         two = arr[i]+arr[j]
#         st = bisect.bisect_left(arr,-two,lo=j+1)  #lo hi로 범위설정가능
#         en = bisect.bisect_right(arr,-two,lo=j+1)
#         cnt += en-st
# print(cnt)



#이분탐색으로는 시간 부족해서 안풀린듯

import sys
input = sys.stdin.readline
def threeSum(n, nums):
    nums.sort()
    cnt = 0
    for i, ans1 in enumerate(nums):
        st, en = i+1, n-1

        while st<en:
            sum_3 = ans1+nums[st]+nums[en]
            if sum_3<0: st += 1
            elif sum_3>0: en -= 1
            elif nums[st] != nums[en]:
                dup_st = 1
                dup_en = 1
                st += 1
                en -= 1
                while nums[st] == nums[st-1]:
                    st += 1
                    dup_st += 1
                while nums[en] == nums[en+1]:
                    en -= 1
                    dup_en += 1
                cnt += dup_st*dup_en

            else:   #en-st+1
                c= en-st+1
                cnt += (c*(c-1))//2
                break
    return cnt

n = int(input())
nums = list(map(int,input().split()))
print(threeSum(n, nums))
##################################
# import sys
# input = sys.stdin.readline

# n = int(input())
# v = list(map(int,input().split()))
# ans, cnt = 0, [0] * 40001; v.sort()

# for i in range(n):
#     ans += cnt[20000 - v[i]]
#     for j in range(i):
#         cnt[20000 + v[i] + v[j]] += 1
# print(ans)
# ##################################
#이해가 안가는코드