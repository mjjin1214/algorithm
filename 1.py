import sys
sys.stdin = open('input1.txt')


def bfs(x):
    global visit, V
    enqueue(x)
    while front != rear:
        now = dequeue()
        for j in range(V+1):
            if matrix[now][j] == 1 and visit & (1<<j) == 0:
                if j == x:
                    return True
                visit ^= (1 << j)
                enqueue(j)

    return False


def enqueue(x):
    global rear
    rear += 1
    if rear >= 1000:
        rear = 0
    queue[rear] = x


def dequeue():
    global front
    front += 1
    if front >= 1000:
        front = 0
    return queue[front]


queue = [0] * 1000
T = int(input())
for t in range(T):
    V, E = map(int, input().split())
    data = [0]*E
    for e in range(E):
        data[e] = list(map(int, input().split()))

    data.sort(key=lambda x: x[2])
    matrix = [[0]*(V+1) for _ in range(V+1)]
    count = 0
    cnt = 0
    for i in range(len(data)):
        matrix[data[i][0]][data[i][1]] = 1
        for k in range(V):
            front = rear = -1
            visit = 0
            if bfs(k):
                matrix[data[i][0]][data[i][1]] = 0
                break
        else:
            count += data[i][2]
            cnt += 1
            if cnt >= V:
                break

    print('#{} {}'.format(t+1, count))
