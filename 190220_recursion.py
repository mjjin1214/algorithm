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


def hanoi()
