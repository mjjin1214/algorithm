import sys
sys.stdin = open('input3.txt')


def fact(a):
    b = 1
    while a > 1:
        b *= a
        a -= 1

    return b


def backtrack(l, r):
    global N, count, sumd, visit
    for i in range(N):
        if not visit & (1<<i):
            if l + data[i] >= sumd:
                nvis = N - 1
                for j in range(N):
                    if visit & (1 << j):
                        nvis -= 1

                count += 2 ** nvis * fact(nvis)
            else:
                visit ^= (1 << i)
                backtrack(l+data[i], r)
                visit ^= (1 << i)
            if l >= r + data[i]:
                visit ^= (1 << i)
                backtrack(l, r +data[i])
                visit ^= (1 << i)


T = int(input())
for t in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    sumd = (sum(data) + 1) // 2
    visit = count = 0
    backtrack(0, 0)
    print('#{} {}'.format(t + 1, count))
