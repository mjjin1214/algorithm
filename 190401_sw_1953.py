import sys
sys.stdin = open('input2.txt')


def bfs():
    global L, N, M
    while queue:
        y, x, time = queue.pop(0)
        if time > L:
            return
        if data[y][x] == 1:
            for i in range(4):
                if 0 <= y + dy[i] < N and 0 <= x + dx[i] < M and data[y+dy[i]][x+dx[i]] > 0:
                    if i == 0:
                        if data[y+dy[i]][x+dx[i]] != 3 and data[y+dy[i]][x+dx[i]] != 4 and data[y+dy[i]][x+dx[i]] != 7:
                                queue.append((y+dy[i], x+dx[i], time+1))
                    elif i == 1:
                        if data[y+dy[i]][x+dx[i]] != 2 and data[y+dy[i]][x+dx[i]] != 4 and data[y+dy[i]][x+dx[i]] != 5:
                                queue.append((y+dy[i], x+dx[i], time+1))
                    elif i == 2:
                        if data[y+dy[i]][x+dx[i]] != 3 and data[y+dy[i]][x+dx[i]] != 5 and data[y+dy[i]][x+dx[i]] != 6:
                                queue.append((y+dy[i], x+dx[i], time+1))
                    elif i == 3:
                        if data[y+dy[i]][x+dx[i]] != 2 and data[y+dy[i]][x+dx[i]] != 6 and data[y+dy[i]][x+dx[i]] != 7:
                                queue.append((y+dy[i], x+dx[i], time+1))

        elif data[y][x] == 2:
            for i in range(0, 4, 2):
                if 0 <= y + dy[i] < N and 0 <= x + dx[i] < M and data[y+dy[i]][x+dx[i]] > 0:
                    if i == 0:
                        if data[y+dy[i]][x+dx[i]] != 3 and data[y+dy[i]][x+dx[i]] != 4 and data[y+dy[i]][x+dx[i]] != 7:
                                queue.append((y+dy[i], x+dx[i], time+1))
                    elif i == 2:
                        if data[y+dy[i]][x+dx[i]] != 3 and data[y+dy[i]][x+dx[i]] != 5 and data[y+dy[i]][x+dx[i]] != 6:
                                queue.append((y+dy[i], x+dx[i], time+1))

        elif data[y][x] == 3:
            for i in range(1, 4, 2):
                if 0 <= y + dy[i] < N and 0 <= x + dx[i] < M and data[y+dy[i]][x+dx[i]] > 0:
                    if i == 1:
                        if data[y+dy[i]][x+dx[i]] != 2 and data[y+dy[i]][x+dx[i]] != 4 and data[y+dy[i]][x+dx[i]] != 5:
                                queue.append((y+dy[i], x+dx[i], time+1))
                    elif i == 3:
                        if data[y+dy[i]][x+dx[i]] != 2 and data[y+dy[i]][x+dx[i]] != 6 and data[y+dy[i]][x+dx[i]] != 7:
                                queue.append((y+dy[i], x+dx[i], time+1))

        elif data[y][x] == 4:
            for i in range(0, 2):
                if 0 <= y + dy[i] < N and 0 <= x + dx[i] < M and data[y+dy[i]][x+dx[i]] > 0:
                    if i == 0:
                        if data[y+dy[i]][x+dx[i]] != 3 and data[y+dy[i]][x+dx[i]] != 4 and data[y+dy[i]][x+dx[i]] != 7:
                                queue.append((y+dy[i], x+dx[i], time+1))
                    elif i == 1:
                        if data[y+dy[i]][x+dx[i]] != 2 and data[y+dy[i]][x+dx[i]] != 4 and data[y+dy[i]][x+dx[i]] != 5:
                                queue.append((y+dy[i], x+dx[i], time+1))

        elif data[y][x] == 5:
            for i in range(1, 3):
                if 0 <= y + dy[i] < N and 0 <= x + dx[i] < M and data[y+dy[i]][x+dx[i]] > 0:
                    if i == 1:
                        if data[y+dy[i]][x+dx[i]] != 2 and data[y+dy[i]][x+dx[i]] != 4 and data[y+dy[i]][x+dx[i]] != 5:
                                queue.append((y+dy[i], x+dx[i], time+1))
                    elif i == 2:
                        if data[y+dy[i]][x+dx[i]] != 3 and data[y+dy[i]][x+dx[i]] != 5 and data[y+dy[i]][x+dx[i]] != 6:
                                queue.append((y+dy[i], x+dx[i], time+1))

        elif data[y][x] == 6:
            for i in range(2, 4):
                if 0 <= y + dy[i] < N and 0 <= x + dx[i] < M and data[y+dy[i]][x+dx[i]] > 0:
                    if i == 2:
                        if data[y+dy[i]][x+dx[i]] != 3 and data[y+dy[i]][x+dx[i]] != 5 and data[y+dy[i]][x+dx[i]] != 6:
                                queue.append((y+dy[i], x+dx[i], time+1))
                    elif i == 3:
                        if data[y+dy[i]][x+dx[i]] != 2 and data[y+dy[i]][x+dx[i]] != 6 and data[y+dy[i]][x+dx[i]] != 7:
                                queue.append((y+dy[i], x+dx[i], time+1))

        elif data[y][x] == 7:
            for i in range(0, 4, 3):
                if 0 <= y + dy[i] < N and 0 <= x + dx[i] < M and data[y+dy[i]][x+dx[i]] > 0:
                    if i == 0:
                        if data[y+dy[i]][x+dx[i]] != 3 and data[y+dy[i]][x+dx[i]] != 4 and data[y+dy[i]][x+dx[i]] != 7:
                                queue.append((y+dy[i], x+dx[i], time+1))
                    elif i == 3:
                        if data[y+dy[i]][x+dx[i]] != 2 and data[y+dy[i]][x+dx[i]] != 6 and data[y+dy[i]][x+dx[i]] != 7:
                                queue.append((y+dy[i], x+dx[i], time+1))

        data[y][x] = 8


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
T = int(input())
for t in range(T):
    N, M, R, C, L = map(int, input().split())
    data = [[] for _ in range(N)]
    for n in range(N):
        data[n] = list(map(int, input().split()))

    queue = []
    queue.append((R, C, 1))
    bfs()
    count = 0
    for d in data:
        count += d.count(8)

    print('#{} {}'.format(t+1, count))
