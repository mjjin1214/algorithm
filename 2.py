import sys
sys.stdin = open('input2.txt')


def subset(visit, k, n):
    global N, min_sum
    if n == N//2:
        x = y = 0
        for i in range(N):
            if visit & (1<<i):
                x += data[i][0]
                y += data[i][1]
            else:
                x -= data[i][0]
                y -= data[i][1]

        if min_sum > x**2+y**2:
            min_sum = x**2+y**2
        return
    elif m==N//2:

    if k >= N:
        return
    if N-k+n < N//2:
        return
    subset(visit ^ (1<<k), k+1, n+1,m)
    subset(visit, k+1, n,m+1)


T = int(input())
for t in range(T):
    N = int(input())
    data = [() for _ in range(N)]
    for n in range(N):
        data[n] = tuple(map(int, input().split()))

    visit = 0
    min_sum = 9999999999999
    subset(0, 0, 0)
    print('#{} {}'.format(t+1, min_sum))
