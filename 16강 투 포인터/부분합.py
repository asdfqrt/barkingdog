import sys
input = sys.stdin.readline

n,s = map(int,input().split())
arr = list(map(int,input().split()))

st=0
en=0
minlen=sys.maxsize
localsum=arr[0]

while st<=en<n:

    if localsum >= s:
        minlen = min(minlen,en-st+1)
        
        localsum -= arr[st]
        st += 1
        
    else:
        en += 1
        if en!=n: localsum += arr[en]
print(minlen if minlen != sys.maxsize else 0)
            

