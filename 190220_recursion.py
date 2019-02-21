def stair(n):
    global count
    if n < 0:
        return
    elif n == 0:
        count += 1
        return
    stair(n-1)
    stair(n-2)
    return


count = 0
stair(4)
print(count)


def hanoi(fro, spare, to):
    count += 1
    if fro == 1:
        return
    hanoi(fro-1, spare+1, to)
    hanoi(spare+1, fro-1, to)
    return