A,B,C = map(int, input().split())

def power(A,B,C):
    if B==1:
        return A % C
    val = power(A, int(B/2), C)
    val = val * val % C
    if B%2 == 0:
        return val
    return val * A % C
    


print(power(A,B,C))