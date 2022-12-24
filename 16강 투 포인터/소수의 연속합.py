#자연수 N이 10^6으로 O(N^2)이면 시간제한2초 훌쩍 넘어버림, 근데 소수 구하는 체 계산을 하는게 N까지의 모든수로 다 나누는거 아닌가??? 이미 O(N^2) >> 더 좋은 알고리즘이 O(root(n))
#x 숫자가 소수인지 아닌지 확인하는 시간 O(root(x)) * 1~n까지 n O(n) root 10^9 1초빠듯한듯??
#ㄴㄴㄴ에라토스테네스의 체 알고리즘은 O(Nlog(logN)) > 사실상 O(N)에 가까움
# def prime(n):
#     i = 2
#     while i**2 <= n:
#         if n%i == 0: return False
#         i += 1
#     return True

# primelist = []
# for i in range(2,n+1):
#     if prime(i):
#         primelist.append(i)



n = int(input())

def prime(n):
    array = [True for i in range(n+1)]
    for i in range(2, int(n**(1/2))+1):
        if array[i] == True:
            for j in range(i+i,n,i):
                array[j] = False

    return [i for i in range(2, n+1) if array[i]]

primelist = prime(n)

st = 0
en = 0
plen = len(primelist)
localsum = 2
cnt = 0
while st<plen and en<plen:
    if localsum == n:
        cnt += 1
        st +=1
        en +=1
        if st<plen and en<plen: localsum += primelist[en] - primelist[st-1]
    elif localsum < n:
        en +=1
        if en<plen: localsum += primelist[en]
    else:
        st += 1
        if st<plen: localsum -= primelist[st-1]
print(cnt)
        
