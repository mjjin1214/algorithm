import sys

sys.stdin = open('input.txt', 'r')


def bfs(here):
    global front, rear
    rear += 1
    queue[rear] = here
    visited[here] = True
    while front != rear:
        front += 1
        here = queue[front]
        print(here)
        for next in range(max(data)+1):
            if matrix[here][next] and not visited[next]:
                visited[next] = True
                distance[next] = distance[here] + 1
                parent[next] = here
                rear += 1
                queue[rear] = next


data = list(map(int, input().split()))
queue = [0]*1000
front = rear = -1
visited = [0]*(max(data)+1)
distance = [0]*(max(data)+1)
parent = [-1]*(max(data)+1)
matrix = [[0 for _ in range(max(data)+1)] for _ in range(max(data)+1)]
for i in range(0, len(data), 2):
    matrix[data[i]][data[i+1]] = 1

bfs(1)