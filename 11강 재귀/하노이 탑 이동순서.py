def hanoi(N,from_pos,to_pos):
    if N == 1:
        print(from_pos, to_pos)
        return

    hanoi(N-1,from_pos,6-from_pos-to_pos)
    print(from_pos, to_pos)
    hanoi(N-1,6-from_pos-to_pos,to_pos)


N = int(input())
print((1<<N)-1)
hanoi(N,1,3)