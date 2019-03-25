import sys

sys.stdin = open('input1.txt')


def power1(a, x):
    if x == 0:
        return 1
    elif x == 1:
        return a
    elif x & 1:
        return power1(a, x - 1) * a
    else:
        temp = power1(a, x // 2)
        return temp * temp


def power2(a, x):
    global ans
    while x:
        if x & 1:
            ans *= a
        a = a * a
        x >>= 1


ans = 1
power2(2, 10)
print(power1(2, 10), ans)