import sys
sys.stdin = open('input3.txt')


def fact(a):
    b = 1
    while a > 1:
        b *= a
        a -= 1

    return b


def bfs():
    global N, count, sumd
    while front != rear:
        l, r, vis = dequeue()
        if vis == (1 << N) - 1:
            count += 1
            continue

        for i in range(N):
            if not vis & (1<<i):
                if l+data[i] >= sumd:
                    nvis = N-1
                    for j in range(N):
                        if vis & (1 << j):
                            nvis -= 1

                    count += 2 ** nvis * fact(nvis)
                else:
                    enqueue((l+data[i], r, vis ^ (1<<i)))
                if l >= r+data[i]:
                    enqueue((l, r+data[i], vis ^ (1<<i)))


def enqueue(a):
    global rear
    rear += 1
    if rear >= 800000:
        rear = 0
    queue[rear] = a


def dequeue():
    global front
    front += 1
    if front >= 800000:
        front = 0
    return queue[front]


queue = [0]*800000
front = rear = -1
T = int(input())
for t in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    sumd = (sum(data)+1) // 2
    visit = 0
    count = 0
    for n in range(N):
        enqueue((data[n], 0, visit ^ (1<<n)))
        bfs()

    print('#{} {}'.format(t+1, count))
