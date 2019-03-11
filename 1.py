import sys

sys.stdin = open('input.txt', 'r')


def up(N, S):
    for x in range(N):
        queue = [0]*N
        rear = 0
        i = 0
        y = 0
        while y < N:
            print('{}, rear {}, i {}, y {}'.format(queue, rear, i, y))
            if Data[y][x]:
                if queue[rear]:
                    if queue[rear] == Data[y][x]:
                        Data[i][x] = queue[rear] * 2
                        y += 1
                        i += 1
                        rear += 1
                    else:
                        Data[i][x] = queue[rear]
                        i += 1
                        rear += 1
                        queue[rear] = Data[y][x]
                else:
                    queue[rear] = Data[y][x]
            y += 1

        for j in range(i+1, N):
            Data[j][x] = 0


T = int(input())
for t in range(T):
    N, S = input().split()
    N = int(N)
    Data = [[] for _ in range(N)]
    for n in range(N):
        Data[n] = list(map(int, input().split()))

    up(N, S)
    for d in Data:
        print(d)
