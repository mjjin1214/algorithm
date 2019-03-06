import sys
sys.stdin = open('input.txt', 'r')


def dfs():
    global height, width
    stack.append([0, 0])
    Data[0][0] = 2
    while stack:
        now = stack[-1]
        for i in range(4):
            if 0 <= now[0] + dy[i] < height and 0 <= now[1] + dx[i] < width and Data[now[0] + dy[i]][now[1] + dx[i]] != 2:
                if Data[now[0] + dy[i]][now[1] + dx[i]] == 1:
                    Data[now[0] + dy[i]][now[1] + dx[i]] = 2
                else:
                    stack.append([now[0] + dy[i], now[1] + dx[i]])
                    Data[now[0] + dy[i]][now[1] + dx[i]] = 2
                    break
        else:
            stack.pop(-1)


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
height, width = map(int, sys.stdin.readline().split())
Data = []
for _ in range(height):
    data = list(map(int, sys.stdin.readline().split()))
    Data.append(data)

stack = []
cheese = count = answer = 0
for y in range(height):
    for x in range(width):
        if Data[y][x] == 1:
            cheese += 1

while cheese > 0:
    answer = cheese
    cheese = 0
    dfs()
    for y in range(height):
        for x in range(width):
            if Data[y][x] == 1:
                cheese += 1
            if Data[y][x] == 2:
                Data[y][x] = 0

    count += 1

print('{}\n{}'.format(count, answer))
