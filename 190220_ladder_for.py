import sys

sys.stdin = open('input.txt', 'r')

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
            y = 99
            check_matrix = [[0 for _ in range(100)] for _ in range(100)]
            while True:
                if y == 0:
                    break
                check_matrix[y][x] = 1
                for i in range(3):
                    if -1 < x+dx[i] < 100 and -1 < y+dy[i] < 100 and check_matrix[y+dy[i]][x+dx[i]] == 0 and ladders[y+dy[i]][x+dx[i]] != 0:
                        y += dy[i]
                        x += dx[i]
                        break
            print(f'#{t} {x}')
            break
