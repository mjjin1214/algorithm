import sys
sys.stdin = open('input3.txt')


def bfs():
    while front != rear:
        y, x, k, num = dequeue()
        for i in range(4):
            if 0 <= y + dy[i] < 4 and 0 <= x + dx[i] < 4:
                if k == 6:
                    answer.add(num+data[y+dy[i]][x+dx[i]])
                    continue
                enqueue((y+dy[i], x+dx[i], k+1, num+data[y+dy[i]][x+dx[i]]))


def enqueue(a):
    global rear
    rear += 1
    if rear >= 1000:
        rear = 0
    queue[rear] = a


def dequeue():
    global front
    front += 1
    if front >= 1000:
        front = 0
    return queue[front]


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
queue = [0]*1000
front = rear = -1
data = [[] for _ in range(4)]
T = int(input())
for t in range(T):
    for d in range(4):
        data[d] = input().split()

    answer = set()
    for y in range(4):
        for x in range(4):
            enqueue((y, x, 1, data[y][x]))
            bfs()

    print('#{} {}'.format(t+1, len(answer)))