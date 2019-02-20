import sys

sys.stdin = open('input.txt', 'r')


def dfs(y, x):
    if y == 0:
        global col
        col = x
        return col
    check_matrix[y][x] = 1
    for i in range(3):
        if -1 < x+dx[i] < 100 and -1 < y+dy[i] < 100 and check_matrix[y+dy[i]][x+dx[i]] == 0 and ladders[y+dy[i]][x+dx[i]] != 0:
            dfs(y+dy[i], x+dx[i])
            return

dx = [-1, 1, 0]
dy = [0, 0, -1]

for _ in range(10):
    t = input()
    ladders = []
    for _ in range(100):
        ladder = list(map(int, input().split()))
        ladders.append(ladder)

    count = 0
    for x in range(len(ladders[99])-1, -1, -1):
        if ladders[99][x] == 2:
            check_matrix = [[0 for _ in range(100)] for _ in range(100)]
            dfs(99, x)
            print(f'#{t} {col}')
