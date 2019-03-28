import sys
sys.stdin = open('input1.txt')


def bfs(0):
    global visit, N
    while queue:
        y, x = dequeue()
        for i in range(4):
            if 0 <= y+dy[i] < N and 0 <= x+dx[i] < N and not visit[y+dy[i]] & (1<<x):
                if matrix[y+dy[i]][x+dx[i]] > matrix[y+dy[i]][x+dx[i]] - matrix[y][x] + 1:
                    matrix[y + dy[i]][x + dx[i]] = matrix[y+dy[i]][x+dx[i]] - matrix[y][x] + 1
        min_cost = 9999999
        min_index = 0
        for j in range(4):
            if min_cost > matrix[y+dy[j]][x+dx[j]]:
                min_cost = matrix[y+dy[j]][x+dx[j]]
                min_index = (y+dy[j], x+dx[j])


def enqueue(y, x):
    global rear
    rear += 1
    if rear >= 1000000:
        rear = 0
    queue[rear] = (y, x)


def dequeue():
    global front
    front += 1
    if front >= 1000000:
        front = 0
    return queue[front]


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
queue = [0]*1000000
T = int(input())
for t in range(T):
    N = int(input())
    data = [[] for _ in range(N)]
    for n in range(N):
        data[n] = list(map(int, input().split()))

    visit = [0] * N
    front = rear = -1
    matrix = [[9999]*N for _ in range(N)]
    matrix[0][0] = 0
    visit[0] ^= (1 << 0)
    enqueue((0, 0))
    bfs()
    print('#{} {}'.format(t+1, count))
