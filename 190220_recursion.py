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
    if fro == 0:
        return
    global count
    count += 1
    hanoi(fro-1, to, spare)
    hanoi(fro-1, spare, to)
    return


count = 0
hanoi(3)
print(count)