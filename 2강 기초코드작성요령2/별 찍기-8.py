N = int(input())
for i in range(N):
    print("*" * (i+1) + " " * 2*(N-i-1) + "*" * (i+1))
for i in range(1,N):
    print("*" * (N-i) + " " * 2*i + "*"*(N-i))